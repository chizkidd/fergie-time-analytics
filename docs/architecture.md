# System Architecture

## Overview

Fergie Time is an interactive football decision-simulation application. It combines historical match data, a simulation engine, decision evaluation, and a browser-based interface.

The production implementation is private. This document describes the system at a conceptual level.

## Main components

### 1. Historical match data

The application uses historical Premier League match-event data, including:

- Match results and scores
- Match clock and event timing
- Starting lineups and substitutions
- Shot locations and expected-goal values
- Player information

The data provides the historical context from which a scenario begins.

### 2. Match-state representation

A scenario represents a match at a particular point in time.

Relevant state information includes:

- Current score
- Match minute
- Team and player availability
- Red cards
- Remaining substitutions
- Historical events already observed

The distinction between the observed past and simulated future is maintained throughout the application.

### 3. Decision simulation

The user selects a tactical instruction or combination of instructions.

The simulation evaluates the possible continuation of the match under each legal option. Each option is evaluated repeatedly to estimate its outcome distribution.

### 4. Decision evaluation

The system summarizes each option using:

- Expected points
- Win probability
- Draw probability
- Loss probability
- Outcome variance
- Difference from the strongest available option

The evaluation also accounts for simulation uncertainty. Small numerical differences are not automatically interpreted as meaningful differences.

### 5. User interface

The browser interface allows users to:

- Enter a historical match scenario
- Inspect the score, clock, and lineups
- Select tactical instructions
- View the decision evaluation
- Watch a simulated continuation
- Review the final decision report

The simulation runs separately from the main interface using a Web Worker.

## Conceptual data flow

```mermaid
flowchart TD
    A[Historical match-event data] --> B[Scenario construction]
    B --> C[Observed match state]
    C --> D[Candidate tactical decisions]
    D --> E[Monte Carlo simulation]
    E --> F[Outcome distributions]
    F --> G[Uncertainty-aware comparison]
    G --> H[Decision report]
    H --> I[Interactive browser interface]
````

## Important architectural distinction

The historical match and the simulated continuation serve different purposes.

- Historical events establish what actually happened.
- The simulation estimates possible futures from a historical state.
- The interface communicates which information is observed and which is simulated.

The application does not claim that a counterfactual simulation is a replay of an alternative historical reality.