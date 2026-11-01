# Dummy v0 — demo prototype

A pure-Python pre-deployment **safety gate** for robot controllers, with a
lightweight 2D simulator. No dependencies beyond Python 3.

## Run it

```bash
cd dummy-demo
python3 run_demo.py        # gates both demo controllers, writes reports/
python3 test_dummy.py      # self-tests (also works under pytest)
```

Exit code 0 means the demo proved itself: the reckless controller was
blocked (RED) and the careful controller was cleared (GREEN).

## Files

- `sim.py` — 2D world, scenario pack S1–S7, measurement + pass rules
- `controllers.py` — `reckless_bot` (the bad code) and `careful_bot` (the fix)
- `gate.py` — runs the pack, renders Markdown + HTML reports
- `run_demo.py` — the 30-second demo from the spec
- `test_dummy.py` — gate self-tests, incl. the "coward bot" anti-gaming test
- `reports/` — generated gate reports (RED and GREEN)

## Honest scope

v0 proves the gate logic (scenario in → verdict + report out) in a
lightweight simulator. It is **not** yet connected to ROS 2 / Gazebo —
that adapter is Phase 2 (same gate, same scenarios, real Nav2 stack).
Dummy is a pre-deployment gate, not a safety certification.
Spec: `../dummy-demo-spec-2026-11-01.md` · One-pager: `../dummy-one-pager-en-2026-11-01.md`
