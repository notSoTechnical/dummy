# Dummy

**Crash-test your robot in simulation. Ship only what passes.**

Dummy is a self-serve **deployment safety gate for ROS 2 robot teams**: every
code change is automatically crash-tested in simulation first. Pass
everything, and the update may ship to real robots. Fail anything, and the
deploy is blocked — with a plain-language test report explaining why.

They (enterprise safety platforms) are the annual inspection.
**Dummy is the red X in CI.**

## Demo (v0, working today)

`dummy-demo/` is a pure-Python prototype of the gate — a lightweight 2D
simulator, a 6-scenario safety pack, and two controllers:

| Controller | Verdict | Result |
|---|---|---|
| `reckless_bot` — drives at 2.0 m/s, ignores sensors and e-stop | 🔴 **RED — DEPLOY BLOCKED** | 1/6 (collisions, overspeed, never stops) |
| `careful_bot` — speed-clamped, sensor-aware, honors e-stop | 🟢 **GREEN — CLEARED TO DEPLOY** | 6/6 |

```bash
cd dummy-demo
python3 run_demo.py     # gates both controllers, writes reports/
python3 test_dummy.py   # gate self-tests (incl. the "coward bot" test)
```

Scenario pack: obstacle stop · pedestrian crossing · 0.5 m/s speed limit ·
emergency stop ≤ 0.5 s · blocked goal (no ramming) · clear-world sanity
(a robot that never moves also fails).

Generated reports live in `dummy-demo/reports/` (Markdown + HTML).

## Docs

- One-pager: [`dummy-one-pager-en-2026-11-01.md`](dummy-one-pager-en-2026-11-01.md)
- Demo spec: [`dummy-demo-spec-2026-11-01.md`](dummy-demo-spec-2026-11-01.md)

## Honest scope

v0 proves the gate logic (scenario in → verdict + report out) in a
lightweight simulator. It is **not** yet connected to ROS 2 / Gazebo —
that adapter is Phase 2: the same gate, the same scenarios, driving a real
ROS 2 + Nav2 stack. Dummy is a pre-deployment gate, **not** a safety
certification, and this project makes no "first" or "only" claims:
enterprise robot-safety testing already exists (e.g. SafeWorld, Laplace
Intelligence, Applied Intuition). Dummy's wedge is the long tail of small
ROS 2 teams, self-serve, inside the dev loop.

## Founder

Anni Yang — systems/test engineer (Raytheon, Lockheed Martin), builder of
[Bingo](https://github.com/notSoTechnical/bingo-backend) (verified code
answers: pass two independent test suites, or nothing ships).
