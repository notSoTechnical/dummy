"""Tests for Dummy v0 — run with: python3 -m pytest test_dummy.py
(or plain: python3 test_dummy.py)
"""
import math

from controllers import CarefulBot, RecklessBot, clamp_speed
from gate import run_gate


def test_clamp_speed():
    vx, vy = clamp_speed(2.0, 0.0)
    assert abs(vx - 0.5) < 1e-9 and vy == 0.0
    assert clamp_speed(0.2, 0.0) == (0.2, 0.0)


def test_reckless_bot_is_blocked():
    green, results = run_gate(RecklessBot())
    assert green is False
    failed = {r.scenario for r in results if not r.passed}
    # Must be caught on collision, speed and e-stop grounds at minimum.
    assert {"S1", "S3", "S4", "S5"} <= failed, failed


def test_careful_bot_is_cleared():
    green, results = run_gate(CarefulBot())
    assert green is True, [(r.scenario, r.detail) for r in results if not r.passed]


def test_camera_only_bot_fails_night_run():
    # Yesterday's "fixed" controller: trusts the main sensor only, never
    # slows down at night. In the dark it cannot see the black cart at all.
    class CameraOnlyBot:
        name = "camera_only_bot"
        def step(self, obs):
            if obs.estop:
                return 0.0, 0.0
            if obs.gap < 0.45:
                return 0.0, 0.0
            dx, dy = obs.goal_x - obs.x, obs.goal_y - obs.y
            d = math.hypot(dx, dy)
            if d <= 0.3:
                return 0.0, 0.0
            return 0.5 * dx / d, 0.5 * dy / d
    green, results = run_gate(CameraOnlyBot())
    assert green is False
    s7 = [r for r in results if r.scenario == "S7"][0]
    assert s7.passed is False and s7.collided is True


def test_coward_bot_would_fail_s6():
    class CowardBot:
        name = "coward_bot"
        def step(self, obs):
            return 0.0, 0.0
    green, results = run_gate(CowardBot())
    assert green is False
    s6 = [r for r in results if r.scenario == "S6"][0]
    assert s6.passed is False  # safe-but-useless is still a fail


if __name__ == "__main__":
    test_clamp_speed()
    test_reckless_bot_is_blocked()
    test_careful_bot_is_cleared()
    test_camera_only_bot_fails_night_run()
    test_coward_bot_would_fail_s6()
    print("all tests passed")
