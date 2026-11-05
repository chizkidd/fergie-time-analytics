# Fergie Time: Premier League Football Analytics & Decision Simulation

**An interactive Premier League decision-simulation game exploring tactical choices, Monte Carlo methods, and historical model evaluation.**

[**Play Fergie Time**](https://fergie-time.pages.dev/)

Fergie Time puts you in charge of a real Premier League match during its closing stages. You make tactical decisions, simulate their possible consequences, and compare options using expected points, outcome probabilities, and uncertainty estimates.

This repository is a public technical showcase of selected analytical methods, evaluation findings, and reproducible examples. It does not contain the production application source code or the proprietary simulation engine.


## Application preview

> **BEGINNING GAME STATE**

![Fergie Time match start interface](assets/gameplay.png)

## The problem

Given a football match's current state, how can we compare alternative tactical decisions when the eventual outcome is uncertain?

A single simulated result is not enough. A useful comparison needs to account for the distribution of possible outcomes, the uncertainty in estimated differences, and the trade-offs between winning, drawing, and losing.

Fergie Time explores this problem using historical Premier League match-event data and Monte Carlo simulation.

## What the application evaluates

The application uses historical match-event information, including match results, lineups, shots, shot locations, and player information.

For each legal tactical option, the simulation estimates:

- Expected points, using 3 points for a win, 1 for a draw, and 0 for a loss.
- Win, draw, and loss probabilities.
- Outcome variability and risk.
- Differences between candidate decisions.
- Whether estimated differences are distinguishable from simulation noise.

The production application is documented as evaluating each legal option with 1,000 simulations.

## Analytical methods

The project brings together several statistical and engineering ideas:

1. **Monte Carlo simulation:** Repeatedly simulate possible match continuations to estimate outcome distributions.
2. **Common random numbers:** Use shared random inputs across candidate decisions to reduce noise in paired comparisons when the resulting outcomes are positively correlated.
3. **Uncertainty-aware comparison:** Estimate the uncertainty of paired differences rather than treating every numerical ranking as meaningful.
4. **Multi-objective reporting:** Present expected points alongside win, draw, and loss probabilities.
5. **Historical backtesting:** Compare simulated continuations with observed historical match outcomes.
6. **Population and temporal diagnostics:** Examine differences across match situations and seasons rather than relying exclusively on aggregate metrics.

See the [simulation methodology](docs/simulation-methodology.md) and [evaluation notes](docs/evaluation.md).

## Historical data diagnostics

The original project documentation reports coverage across 12 Premier League seasons, from 2014/15 through 2025/26:

| Measure | Reported count |
|---|---:|
| Seasons | 12 |
| Matches | 4,560 |
| Shots | 116,004 |
| Match situations | 12,599 |

The production daily pool uses the two most recent seasons. Older seasons are treated as practice scenarios.

The historical data showed meaningful changes across seasons. Average last-shot timing, late-match shot volume, goals after the 90th minute, and substitution usage all varied over time.

The included CSV contains selected season-level descriptive statistics summarized from the original project documentation. These are descriptive diagnostics, not model-performance scores.

## Evaluation and scientific integrity

A central design principle is to distinguish observed match history from simulated counterfactual outcomes.

- Historical events establish what actually happened.
- The simulation estimates possible continuations from a historical match state.
- Simulated outcomes are not presented as observed historical events.

The original evaluation identified discrepancies across multiple historical match-situation groups. The two most recent seasons used by the production daily pool passed the documented evaluation gate, while older seasons did not consistently satisfy it.

A later experimental calibration investigated whether era-specific parameters could improve performance across older seasons. Although it improved some diagnostics, it failed its predeclared validation criteria and was not promoted to production. The shipped engine remains unchanged.

These results matter: passing an aggregate metric does not establish that a model is reliable across every season or match situation.

See [Evaluation and Historical Diagnostics](docs/evaluation.md) for details.

## Repository structure

```text
fergie-time-analytics/
├── README.md
├── COPYRIGHT.md
├── docs/
│   ├── architecture.md
│   ├── simulation-methodology.md
│   ├── evaluation.md
│   └── limitations.md
├── examples/                            # Standalone Python demonstrations using synthetic data
│   ├── monte-carlo-simulation.py
│   └── common-random-numbers.py
├── results/                             # Selected historical descriptive statistics
│   └── historical-season-summary.csv
└── assets/                              # Analytical diagrams and gameplay screenshots
    ├── architecture.mmd
    ├── simulation-workflow.mmd
    ├── architecture.png
    ├── simulation-workflow.png
    ├── gameplay.png
    ├── gameplay-*.png
    └── homepage-*.png
```

## Reproducible examples

The Python examples are independent educational demonstrations. They use synthetic outcome probabilities and do not contain the production simulation engine or proprietary production data.

Install the dependency:

```bash
python -m pip install numpy
```

Run the examples:

```bash
python examples/monte-carlo-simulation.py
python examples/common-random-numbers.py
```

## Technology

The production application uses:

- TypeScript
- React
- Vite
- Node.js
- Web Workers
- Playwright for browser-level testing

The public statistical examples use Python and NumPy.


## Scope and limitations

Fergie Time uses historical match-event data. It does **not** use optical player-tracking data, GPS tracking, or measured player coordinates.

The pitch visualizations are schematic representations of tactical arrangements and player roles, not observed player positions. Ball position is derived from the game state rather than measured from tracking data.

The application is an interactive decision-simulation project. It is not a professional recruitment model, a player-tracking analytics platform, or a substitute for coaching judgment.

See [Limitations and Scope](docs/limitations.md).

## Links

- [Live application](https://fergie-time.pages.dev/)
- [GitHub profile](https://github.com/chizkidd)
- [Technical writing](https://chizkidd.github.io/)
- [Sports writing](https://chizobao.substack.com)

## Data sources and attribution

The production application uses historical football data and supporting player metadata from external sources:

| Source | Data used |
|---|---|
| [Understat](https://understat.com/) | Match results, shots, expected goals (xG), and player participation across the historical dataset. |
| [FPL Core Insights](https://github.com/olbauday/FPL-Core-Insights) | Named benches and shirt numbers for the 2025/26 season. |
| [balldontlie](https://balldontlie.io/) | Player shirt numbers. |
| [FotMob](https://www.fotmob.com/) | Appears to be an upstream source for some FPL Core Insights data; this application does not query FotMob directly. |

The production application prepares its data before publication. Visitors receive preprocessed data files from the application rather than querying these providers directly. The production application therefore distributes source-derived data, not merely references to external websites.

This repo does not include the underlying raw match-event files. Its `historical-season-summary.csv` contains selected season-level descriptive statistics reported in the original project documentation. It does not provide the underlying match-level data or a standalone script to regenerate those statistics.

Source identification and attribution do not establish permission to reuse or redistribute third-party data. Commercial use, automated collection, and redistribution rights have not been independently verified for every source. Consult the providers' terms before reusing or redistributing their data.

## Copyright and licensing

See [COPYRIGHT.md](COPYRIGHT.md) for copyright and licensing information.

## Simulation workflow 

<img src="assets/simulation-workflow.png" alt="Simulation workflow" width="500">

<!-- ![Simulation workflow](assets/simulation-workflow.png) -->

The workflow diagram is maintained in [`assets/simulation-workflow.mmd`](assets/simulation-workflow.mmd).

## Additional application preview

> **FINAL GAME STATE**

![Fergie Time gameplay end interface](assets/gameplay-DECISIONS-FULL.png)

---

> **CHOICES FOR A SINGLE GAME STATE**

![Fergie Time gameplay single game state interface](assets/gameplay-DECISION-SINGLE-FULL.png)

---

> **FINAL PLAY-BY-PLAY REPORT**

![Fergie Time match end play-by-play report](assets/gameplay-PLAY-BY-PLAY.png)

---

> **HOME PAGE**

![Fergie Time Homepage](assets/homepage-FULL.png)



---

_This repository is a technical showcase, not an open-source release of the Fergie Time game application._