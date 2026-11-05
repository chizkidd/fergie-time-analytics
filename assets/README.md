# Assets

## Mermaid Diagrams

Install Mermaid CLI and render both files:

```bash
npx -y @mermaid-js/mermaid-cli -i assets/architecture.mmd -o assets/architecture.png -b transparent

npx -y @mermaid-js/mermaid-cli -i assets/simulation-workflow.mmd -o assets/simulation-workflow.png -b transparent
```

---

## Gameplay Screenshots

Capture these two views if possible:

1. **The match screen:** Show the pitch, scoreboard, lineups, and tactical options.
2. **The decision report:** Show the expected points, probabilities, and comparison between decisions.

You can use `Playwright` to capture the live application:

```bash
npx playwright screenshot --viewport-size="1440,1000" --wait-for-timeout=4000 https://fergie-time.pages.dev/ assets/game-screenshot.png
```

That captures the page at a desktop viewport. For the decision report, open a scenario, make a decision, and capture the actual report manually. Or complete a single full game, and capture the actual report for all decsions. The initial URL screenshot won't necessarily show that state.