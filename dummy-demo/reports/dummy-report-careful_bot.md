# Dummy Gate Report — careful_bot

## Verdict: GREEN — CLEARED TO DEPLOY

7/7 scenarios passed.

| # | Scenario | Result | Closest gap (m) | Top speed (m/s) | Goal reached | Detail |
|---|---|---|---|---|---|---|
| S1 | Obstacle stop | PASS | 0.45 | 0.5 | no | stopped/waited, no collision |
| S2 | Pedestrian crossing | PASS | 0.4 | 0.5 | yes | stopped/waited, no collision |
| S3 | Speed limit (clear world) | PASS | 99.0 | 0.5 | yes | top speed 0.50 m/s (limit 0.5 m/s) |
| S4 | Emergency stop | PASS | 99.0 | 0.5 | no | stopped 0.0s after e-stop, crept 0.00 m |
| S5 | Blocked goal | PASS | 0.45 | 0.5 | no | stopped/waited, no collision |
| S6 | Clear-world sanity (must reach goal) | PASS | 99.0 | 0.5 | yes | goal reached |
| S7 | Night run — dark obstacle | PASS | 0.43 | 0.25 | no | stopped/waited, no collision |

*Dummy v0 — pre-deployment simulation gate. Not a safety certification.*
