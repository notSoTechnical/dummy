"""Dummy v0 — the two demo controllers.

reckless_bot: written in five minutes, never tested. Drives straight at the
goal at 2.0 m/s, ignores its distance sensor, ignores the e-stop.

careful_bot: the fixed version. Clamps speed to the 0.5 m/s limit (the same
clamp taught in ZeroToAIAgent Ep118), reads its sensor every step, stops for
obstacles and pedestrians, honors the e-stop, and waits instead of ramming
a blocked goal.
"""
from __future__ import annotations

import math

SPEED_LIMIT = 0.5
STOP_GAP = 0.45  # stop when the nearest obstacle surface is closer than this


def _toward(obs, speed: float) -> tuple[float, float]:
    dx, dy = obs.goal_x - obs.x, obs.goal_y - obs.y
    d = math.hypot(dx, dy)
    if d < 1e-9:
        return 0.0, 0.0
    return speed * dx / d, speed * dy / d


def clamp_speed(vx: float, vy: float, limit: float = SPEED_LIMIT) -> tuple[float, float]:
    s = math.hypot(vx, vy)
    if s <= limit or s == 0:
        return vx, vy
    return vx * limit / s, vy * limit / s


class RecklessBot:
    name = "reckless_bot"
    CRUISE = 2.0

    def step(self, obs):
        return _toward(obs, self.CRUISE)


class CarefulBot:
    name = "careful_bot"

    def step(self, obs):
        if obs.estop:
            return 0.0, 0.0
        if obs.gap < STOP_GAP:
            return 0.0, 0.0  # wait — never ram
        dx, dy = obs.goal_x - obs.x, obs.goal_y - obs.y
        if math.hypot(dx, dy) <= 0.3:
            return 0.0, 0.0
        vx, vy = _toward(obs, SPEED_LIMIT)
        return clamp_speed(vx, vy)
