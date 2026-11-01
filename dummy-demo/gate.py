"""Dummy v0 — the gate: run every scenario, emit a verdict and a report.

GREEN (all scenarios pass) = cleared to deploy.
RED (any scenario fails) = deploy blocked.
Reports are written as Markdown and as a standalone HTML page.
"""
from __future__ import annotations

import html
from pathlib import Path

from sim import default_scenarios, run_scenario


def run_gate(controller) -> tuple[bool, list]:
    results = [run_scenario(controller, sc) for sc in default_scenarios()]
    return all(r.passed for r in results), results


def render_markdown(controller_name: str, green: bool, results: list) -> str:
    verdict = "GREEN — CLEARED TO DEPLOY" if green else "RED — DEPLOY BLOCKED"
    lines = [
        f"# Dummy Gate Report — {controller_name}",
        "",
        f"## Verdict: {verdict}",
        "",
        f"{sum(r.passed for r in results)}/{len(results)} scenarios passed.",
        "",
        "| # | Scenario | Result | Closest gap (m) | Top speed (m/s) | Goal reached | Detail |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in results:
        lines.append(
            f"| {r.scenario} | {r.title} | {'PASS' if r.passed else '**FAIL**'} "
            f"| {r.min_gap} | {r.max_speed} | {'yes' if r.reached_goal else 'no'} | {r.detail} |")
    lines += ["", "*Dummy v0 — pre-deployment simulation gate. Not a safety certification.*"]
    return "\n".join(lines) + "\n"


def render_html(controller_name: str, green: bool, results: list) -> str:
    color = "#1a9e54" if green else "#d43a2f"
    verdict = "GREEN — CLEARED TO DEPLOY" if green else "RED — DEPLOY BLOCKED"
    rows = ""
    for r in results:
        badge = ('<span style="color:#1a9e54;font-weight:700">PASS</span>' if r.passed
                 else '<span style="color:#d43a2f;font-weight:700">FAIL</span>')
        rows += (f"<tr><td>{r.scenario}</td><td>{html.escape(r.title)}</td><td>{badge}</td>"
                 f"<td>{r.min_gap}</td><td>{r.max_speed}</td>"
                 f"<td>{'yes' if r.reached_goal else 'no'}</td>"
                 f"<td>{html.escape(r.detail)}</td></tr>\n")
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>Dummy Gate Report — {html.escape(controller_name)}</title>
<style>body{{font-family:system-ui,sans-serif;max-width:860px;margin:40px auto;padding:0 20px;color:#111}}
table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #ddd;padding:8px;text-align:left}}
.verdict{{background:{color};color:#fff;padding:16px 20px;border-radius:10px;font-size:22px;font-weight:700}}
</style></head><body>
<h1>Dummy Gate Report — {html.escape(controller_name)}</h1>
<div class="verdict">{verdict}</div>
<p>{sum(r.passed for r in results)}/{len(results)} scenarios passed.</p>
<table><tr><th>#</th><th>Scenario</th><th>Result</th><th>Closest gap (m)</th>
<th>Top speed (m/s)</th><th>Goal reached</th><th>Detail</th></tr>
{rows}</table>
<p><i>Dummy v0 — pre-deployment simulation gate. Not a safety certification.</i></p>
</body></html>
"""


def write_reports(controller, outdir: Path) -> tuple[bool, list]:
    green, results = run_gate(controller)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / f"dummy-report-{controller.name}.md").write_text(
        render_markdown(controller.name, green, results), encoding="utf-8")
    (outdir / f"dummy-report-{controller.name}.html").write_text(
        render_html(controller.name, green, results), encoding="utf-8")
    return green, results
