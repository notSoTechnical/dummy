# Dummy — One-Pager
**Crash-test your robot in simulation. Ship only what passes.**

*Working name (trademark search pending) · Founder: Anni Yang · Nov 1, 2026 · Status: concept approved by founder, pre-demo*

---

## One-liner

Dummy is a self-serve **deployment safety gate for ROS 2 robot teams**: every code change is automatically crash-tested in simulation first. Pass everything, and the update may ship to real robots. Fail anything, and the deploy is blocked — with a plain-language test report explaining why.

## The problem

- Robots are not websites. Bad code cannot be rolled back — it collides, injures, and burns money.
- Robot teams now ship updates weekly or even daily, but testing still means an engineer manually running a few laps in a lab.
- So teams get two bad options: ship slowly (afraid to release), or ship dangerously (under-tested on real hardware).

## Why now

1. **AI is starting to write robot code.** In September 2026, NVIDIA released Isaac ROS 5.0, bringing AI-agent workflows into the ROS ecosystem. The faster code gets generated, the more deployment-time verification becomes the bottleneck. Who verifies agent-written robot code? That is a brand-new question.
2. **Capital has already voted.** Robot safety testing is being funded at scale (see Competition) — the category is validated, but the incumbents all sell to large enterprises.
3. **ROS 2 is now the common foundation.** ROS 1 reached end-of-life in 2025; ROS 2 (Jazzy LTS) plus Gazebo simulation makes "one tool for every ROS 2 team" possible for the first time.

## The product

1. **Connect a repo.** A team connects its ROS 2 project to Dummy (GitHub-style onboarding; target: first test run within 10 minutes).
2. **Every change gets crash-tested.** In Gazebo simulation, Dummy runs a scenario pack: a suddenly appearing obstacle, a pedestrian crossing, a blocked goal point, sensor dropout, emergency-stop response, overspeed-command rejection — with new packs shipped continuously.
3. **A gate, not a dashboard.** Green/red verdict, per-test results, failure replays and logs. **Fail = no deploy** — the same red X developers already respect in software CI.

The first scenario pack covers exactly one category: **ROS 2 + Nav2 mobile robots** (warehouse AGVs, delivery robots). Narrow first, deep first.

## Competition — and our wedge (the honest version)

This space is **not** empty, and the leaders are strong:

- **SafeWorld** (Palo Alto): a robot safety simulation/testing platform that has raised a **$12.2M seed round co-led by a16z Speedrun**, running pilots with large companies in automotive, warehouse automation, and medical devices.
- **Laplace Intelligence**: automated safety stress-testing / AI red-teaming for autonomous vehicles and robots; already generating revenue from autonomous trucking customers, aiming to convert to subscriptions.
- **Applied Intuition**: the established leader in autonomous-system simulation and safety, with the strongest enterprise presence.

**Our wedge — we do not fight them for the same customers:**

| | The incumbents | Dummy |
|---|---|---|
| Customers | Automakers, large enterprises, fleets | **The long tail of ROS 2 teams**: startups, labs, independent robot builders |
| Sales motion | Sales-driven pilots, large contracts | **Self-serve**, developers sign up and pay by card |
| Where it lives | Big pre-deployment validation programs | **Inside the dev loop**: every commit, every release |
| Price tier | Enterprise (six figures to start a conversation) | Developer-tool pricing (below, to be validated) |

In one line: they are the annual safety inspection. **We are the red X in CI.**

## Business model (be the toll, don't sell time)

- **Free**: 1 repo + the basic scenario pack (acquisition + community goodwill).
- **Pro (hypothesis pricing, to be validated in interviews)**: ~$99/mo per repo — full scenario packs, private scenarios, deployment-gate integrations.
- **Team / Fleet**: priced per robot or fleet size. Later: a marketplace for vertical scenario packs (warehousing, agriculture, …) with revenue share.
- The charge point is **a gate every deployment must pass** — recurring by construction, a subscription, not hours.

## Why me (founder–market fit)

- **A career test engineer.** Systems/test engineering at Raytheon (2020–2022) and Lockheed Martin (2022–2025) — Selenium/TestNG, CI/CD, guarding safety-critical systems was my day job for 5+ years.
- **A repeat builder of verification products.** Bingo — code answers that must pass two independent test suites before delivery, with an honest refusal when they can't — is live today. Dummy is the same philosophy, moved onto robots.
- **Built-in distribution.** My channel ZeroToAIAgent is teaching ROS 2 all Season 2 (Ep101–120); the audience is exactly the target user, and every episode is acquisition content.
- **$0 to start.** Pure software + simulation. No hardware, no inventory — a solo founder can reach a revenue signal.

## Proof plan (proof first, applications second)

1. **Demo (~2 weeks):** one unforgettable clip — deliberately broken navigation code gets caught red by Dummy in simulation; the fixed version passes green and ships. Season 2's Ep118–120 teach exactly this stack, so the demo and the content are the same work.
2. **Landing page + waitlist:** one clear page, email capture, channel traffic pointed at it.
3. **10 interviews with ROS 2 teams:** validate the pain and the price point — without assuming they'll buy.
4. **Then apply:** demo + waitlist + interview evidence into the next a16z Speedrun / YC batch. **We are not rushing the Nov 2, 2026 YC deadline** with a newborn idea — blank-essay applications are a tuition we have already paid once.

## Risks (said out loud)

- **Incumbents moving downmarket.** SafeWorld and peers are well funded and could aim at small teams. Our defense is speed, developer experience, and community (the channel) — not secret technology.
- **Simulation ≠ reality.** The sim-to-real gap never fully closes. Our positioning stays honest: Dummy is the **first gate before deployment**, not a safety certification, and never a replacement for real-world testing and compliance.
- **Solo bandwidth.** Job search remains the livelihood main line; this is built in parallel — which is exactly why v1 is scoped to something one person can demo in two weeks.

## Decisions needed from the founder

1. Approve the wedge: **ROS 2 + Nav2 mobile-robot teams only**, narrow first?
2. Keep the working name **Dummy** for now (trademark + domain check before anything public)?
3. If yes, build order: demo spec → landing page → interview list.

---
*Sources verified Nov 1, 2026: SafeWorld $12.2M seed, co-led by a16z Speedrun — startupresearcher.com; Laplace Intelligence revenue and subscription goal — whalesbook.com (reporting its launch); Isaac ROS 5.0 (Sept 2026, ROSCon) — as reported from NVIDIA's release materials. All prices are unvalidated hypotheses. This document makes no "first" or "only" claims.*
