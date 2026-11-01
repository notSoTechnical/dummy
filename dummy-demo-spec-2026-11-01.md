# Dummy — Demo Spec (v0)
*Nov 1, 2026 · Companion to: Dummy One-Pager (EN) · Status: v0 built same day, see "What v0 is / is not"*

## The one clip this demo must produce

> A robot controller that would crash gets a **RED gate: DEPLOY BLOCKED**.
> The fixed controller gets a **GREEN gate: CLEARED TO DEPLOY**.
> Same tests. Same world. The only difference is the code under test.

That 30-second contrast is the whole pitch — for the landing page, the YC/Speedrun application video, and the ROS 2 series finale (Ep118–120).

## What the gate tests (v0 scenario pack — mobile robots)

| # | Scenario | Pass condition | What it catches |
|---|---|---|---|
| S1 | **Obstacle stop** — a box appears 1.2 m ahead on the path to the goal | No collision; robot stops or waits | Controllers that drive blind |
| S2 | **Pedestrian crossing** — a person walks across the robot's path | No collision | Controllers that can't handle moving obstacles |
| S3 | **Speed limit** — the gate watches the robot's actual speed the whole run | Speed never exceeds **0.5 m/s** | Controllers that command dangerous speeds |
| S4 | **E-stop** — an emergency stop fires mid-run | Robot halts within **0.5 s** and stays halted | Controllers that ignore stop commands |
| S5 | **Blocked goal** — the goal point itself is barricaded | No collision; robot must *not* force its way in (stopping and reporting failure = PASS) | Controllers that ram through to "succeed" |
| S6 | **Clear-world sanity** — empty world, reachable goal | Robot actually reaches the goal in time | "Coward" controllers that pass safety tests by never moving |
| S7 | **Night run** — darkness: the main camera/lidar sensor is blind; a black cart (or dark animal) blocks the path | No collision | Controllers that trust one sensor: at night it sees *nothing*. The robot has a short-range bumper sonar (≤0.6 m, works in the dark) — a night-aware controller slows down in low light and trusts the bumper |

*S7 added Nov 1, 2026 at the founder's suggestion ("night vision... so it won't hit a black cart or dark color cats/animals"). It immediately caught a real blind spot: the v0 careful controller — camera-only — fails S7. The night-aware version passes.*

S6 is deliberate: a gate that only punishes movement would certify robots that do nothing. Dummy certifies robots that are **safe AND functional** — the same honesty rule as Bingo (pass both suites, or no delivery).

## The two demo controllers

- **`reckless_bot`** — drives straight at the goal at 2.0 m/s. Ignores its distance sensor. Ignores e-stop. This is the "AI wrote it fast, nobody tested it" controller.
- **`careful_bot`** — clamps speed to the 0.5 m/s limit, reads its distance sensor every step, stops for obstacles and pedestrians, honors e-stop instantly, and if the goal is blocked, waits and reports `blocked` instead of ramming.

## What v0 is / is not (honesty box)

- v0 is a **pure-Python gate + lightweight 2D simulator**. It runs anywhere (no ROS install needed) and proves the product's core logic: scenario in → verdict + report out.
- v0 is **not** yet connected to ROS 2 / Gazebo. That adapter is Phase 2: the same gate, the same scenario definitions, driving a real ROS 2 + Nav2 stack in Gazebo on Ubuntu 24.04 (this machine's OS is already the ROS 2 Jazzy target platform).
- v0 makes **no** safety-certification claim. Dummy is a pre-deployment gate, not a certification.

## The report (the actual product surface)

Every gate run emits a report a non-engineer can read in 20 seconds:
verdict (RED/GREEN) → per-scenario pass/fail with the measured numbers (closest distance, top speed, stop latency, goal reached?) → deploy decision. Reports are generated as Markdown + a standalone HTML page.

## Build order after v0

1. **Phase 2 — ROS adapter**: gate drives turtlesim first (one afternoon), then a Nav2 robot in Gazebo.
2. **Landing page + waitlist** (per one-pager proof plan).
3. **Video**: screen-record the RED→GREEN run; cut into the application + Ep120.
4. **Interviews**: show the report to 10 ROS 2 teams; ask what their gate looks like today (usually: nothing).

## Demo script (30 seconds, for the recording)

1. (0–8s) "This controller was written in five minutes. It drives at full speed and ignores its sensors." → run gate → **S1 FAIL (collision), S3 FAIL (2.0 m/s), S4 FAIL**.
2. (8–15s) "On a real robot, that's a hospital visit. Dummy blocks the deploy." → show RED report.
3. (15–28s) "Same tests, fixed controller." → run gate → **6/6 PASS, GREEN**. "Crash-test your robot in simulation. Ship only what passes."
