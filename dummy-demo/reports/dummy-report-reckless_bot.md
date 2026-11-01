# Dummy Gate Report — reckless_bot

## Verdict: RED — DEPLOY BLOCKED

1/6 scenarios passed.

| # | Scenario | Result | Closest gap (m) | Top speed (m/s) | Goal reached | Detail |
|---|---|---|---|---|---|---|
| S1 | Obstacle stop | **FAIL** | -0.2 | 2.0 | no | collision |
| S2 | Pedestrian crossing | **FAIL** | -0.12 | 2.0 | no | collision |
| S3 | Speed limit (clear world) | **FAIL** | 99.0 | 2.0 | yes | top speed 2.00 m/s (limit 0.5 m/s) |
| S4 | Emergency stop | **FAIL** | 99.0 | 2.0 | yes | never stopped after e-stop |
| S5 | Blocked goal | **FAIL** | -0.05 | 2.0 | no | collision |
| S6 | Clear-world sanity (must reach goal) | PASS | 99.0 | 2.0 | yes | goal reached |

*Dummy v0 — pre-deployment simulation gate. Not a safety certification.*
