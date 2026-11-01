"""Dummy v0 — lightweight 2D robot simulator.

A robot is a circle moving in a plane. A controller under test receives an
observation each step and returns a desired velocity (vx, vy). The world
integrates the motion, tracks collisions, top speed, goal progress and
e-stop compliance. Pure Python, no dependencies.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

ROBOT_RADIUS = 0.25
DT = 0.1  # seconds per step


@dataclass
class Obstacle:
    x: float
    y: float
    r: float
    vx: float = 0.0  # moving obstacles (pedestrian) have a velocity
    vy: float = 0.0


@dataclass
class Observation:
    x: float
    y: float
    goal_x: float
    goal_y: float
    gap: float          # surface distance to the nearest obstacle (inf if none)
    estop: bool         # True once the emergency stop has fired
    t: float


@dataclass
class Scenario:
    name: str
    title: str
    goal: tuple[float, float]
    obstacles: list[Obstacle]
    duration: float                     # max seconds
    estop_at: float | None = None       # when the e-stop fires, if ever
    check: str = ""                     # which pass rule applies


@dataclass
class RunResult:
    scenario: str
    title: str
    passed: bool
    collided: bool
    reached_goal: bool
    max_speed: float
    min_gap: float
    estop_stop_latency: float | None    # seconds from e-stop to full stop
    moved_after_estop: float            # metres travelled after e-stop
    detail: str


def _gap(x: float, y: float, obstacles: list[Obstacle]) -> float:
    best = math.inf
    for o in obstacles:
        d = math.hypot(x - o.x, y - o.y) - ROBOT_RADIUS - o.r
        best = min(best, d)
    return best


def run_scenario(controller, sc: Scenario) -> RunResult:
    """Run one controller through one scenario and measure everything."""
    x, y = 0.0, 0.0
    gx, gy = sc.goal
    obstacles = [Obstacle(o.x, o.y, o.r, o.vx, o.vy) for o in sc.obstacles]
    collided = False
    max_speed = 0.0
    min_gap = _gap(x, y, obstacles)
    reached = False
    estop_time: float | None = None
    stop_time: float | None = None
    dist_after_estop = 0.0
    steps = int(sc.duration / DT)

    for i in range(steps):
        t = i * DT
        estop = sc.estop_at is not None and t >= sc.estop_at
        if estop and estop_time is None:
            estop_time = t
        obs = Observation(x, y, gx, gy, _gap(x, y, obstacles), estop, t)
        vx, vy = controller.step(obs)
        speed = math.hypot(vx, vy)
        max_speed = max(max_speed, speed)
        nx, ny = x + vx * DT, y + vy * DT
        if estop_time is not None:
            dist_after_estop += math.hypot(nx - x, ny - y)
            if stop_time is None and speed <= 0.01 and t >= estop_time:
                stop_time = t
        x, y = nx, ny
        for o in obstacles:
            o.x += o.vx * DT
            o.y += o.vy * DT
        g = _gap(x, y, obstacles)
        min_gap = min(min_gap, g)
        if g < 0:
            collided = True
            break
        if math.hypot(gx - x, gy - y) <= 0.3:
            reached = True
            break

    latency = None
    if estop_time is not None and stop_time is not None:
        latency = round(stop_time - estop_time, 2)

    passed, detail = _judge(sc, collided, reached, max_speed, latency,
                            dist_after_estop)
    return RunResult(sc.name, sc.title, passed, collided, reached,
                     round(max_speed, 2), round(min_gap, 2) if min_gap != math.inf else 99.0,
                     latency, round(dist_after_estop, 2), detail)


SPEED_LIMIT = 0.5


def _judge(sc, collided, reached, max_speed, latency, dist_after_estop):
    if sc.check == "no_collision":
        return (not collided,
                "collision" if collided else "stopped/waited, no collision")
    if sc.check == "speed":
        ok = max_speed <= SPEED_LIMIT + 1e-9
        return ok, f"top speed {max_speed:.2f} m/s (limit {SPEED_LIMIT} m/s)"
    if sc.check == "estop":
        ok = latency is not None and latency <= 0.5 and dist_after_estop <= 0.15
        return ok, (f"stopped {latency}s after e-stop, crept {dist_after_estop:.2f} m"
                    if latency is not None else "never stopped after e-stop")
    if sc.check == "reach":
        return reached, "goal reached" if reached else "goal NOT reached in time"
    raise ValueError(sc.check)


def default_scenarios() -> list[Scenario]:
    return [
        Scenario("S1", "Obstacle stop", (4.0, 0.0),
                 [Obstacle(2.0, 0.0, 0.35)], 12.0, check="no_collision"),
        Scenario("S2", "Pedestrian crossing", (4.0, 0.0),
                 [Obstacle(1.2, -0.35, 0.30, vy=0.5)], 25.0, check="no_collision"),
        Scenario("S3", "Speed limit (clear world)", (6.0, 0.0),
                 [], 20.0, check="speed"),
        Scenario("S4", "Emergency stop", (6.0, 0.0),
                 [], 6.0, estop_at=2.0, check="estop"),
        Scenario("S5", "Blocked goal", (3.0, 0.0),
                 [Obstacle(3.0, 0.0, 0.40)], 12.0, check="no_collision"),
        Scenario("S6", "Clear-world sanity (must reach goal)", (3.0, 0.0),
                 [], 20.0, check="reach"),
    ]
