"""Run the Dummy v0 demo: gate both controllers, print verdicts, write reports.

Usage: python3 run_demo.py
Exit code 0 only if reckless_bot is RED and careful_bot is GREEN —
the demo proving itself.
"""
from pathlib import Path

from controllers import CarefulBot, RecklessBot
from gate import write_reports

OUT = Path(__file__).parent / "reports"


def show(bot) -> bool:
    green, results = write_reports(bot, OUT)
    verdict = "GREEN — CLEARED TO DEPLOY" if green else "RED — DEPLOY BLOCKED"
    print(f"\n{bot.name}: {verdict} ({sum(r.passed for r in results)}/{len(results)} passed)")
    for r in results:
        print(f"  {r.scenario} {r.title}: {'PASS' if r.passed else 'FAIL'} — {r.detail}")
    return green


if __name__ == "__main__":
    reckless_green = show(RecklessBot())
    careful_green = show(CarefulBot())
    ok = (reckless_green is False) and (careful_green is True)
    print("\nDEMO RESULT:", "OK — gate caught the bad code and cleared the good code."
          if ok else "BROKEN — gate verdicts are wrong!")
    raise SystemExit(0 if ok else 1)
