"""
Standalone Monte Carlo example.

Demonstrates:
- Simulating win/draw/loss outcomes.
- Estimating outcome probabilities.
- Calculating expected points.
- Quantifying Monte Carlo uncertainty.

Uses illustrative probabilities, not production Fergie Time parameters.

This version validates its inputs, uses numeric outcomes instead of looping 
over string labels, and reports both simulated and theoretical expected points.
"""

import numpy as np


N_SIMULATIONS = 100_000
SEED = 42

# Outcome order: win, draw, loss.
DECISIONS = {
    "Decision A": np.array([0.35, 0.40, 0.25]),
    "Decision B": np.array([0.40, 0.32, 0.28]),
}

# Three points for a win, one for a draw, zero for a loss.
OUTCOME_POINTS = np.array([3.0, 1.0, 0.0])


def validate_probabilities(probabilities):
    """Check that probabilities form a valid categorical distribution."""
    probabilities = np.asarray(probabilities, dtype=float)

    if probabilities.shape != (3,):
        raise ValueError("Expected exactly three probabilities: win, draw, loss.")

    if not np.all(np.isfinite(probabilities)):
        raise ValueError("Probabilities must be finite.")

    if np.any(probabilities < 0):
        raise ValueError("Probabilities cannot be negative.")

    if not np.isclose(probabilities.sum(), 1.0):
        raise ValueError("Outcome probabilities must sum to 1.")

    return probabilities


def simulate_decision(probabilities, n_simulations, rng):
    """Simulate outcomes and summarize their estimated distribution."""
    probabilities = validate_probabilities(probabilities)

    if n_simulations < 2:
        raise ValueError("At least two simulations are required.")

    # Integer categories: 0 = win, 1 = draw, 2 = loss.
    outcomes = rng.choice(
        3,
        size=n_simulations,
        p=probabilities,
    )

    points = OUTCOME_POINTS[outcomes]

    estimated_probabilities = np.bincount(
        outcomes,
        minlength=3,
    ) / n_simulations

    expected_points = points.mean()
    standard_error = points.std(ddof=1) / np.sqrt(n_simulations)

    theoretical_expected_points = float(
        probabilities @ OUTCOME_POINTS
    )

    return {
        "win_probability": estimated_probabilities[0],
        "draw_probability": estimated_probabilities[1],
        "loss_probability": estimated_probabilities[2],
        "expected_points": expected_points,
        "standard_error": standard_error,
        "theoretical_expected_points": theoretical_expected_points,
    }


def main():
    rng = np.random.default_rng(SEED)

    print(f"Simulations per decision: {N_SIMULATIONS:,}\n")

    results = {}

    for name, probabilities in DECISIONS.items():
        result = simulate_decision(
            probabilities,
            N_SIMULATIONS,
            rng,
        )

        results[name] = result

        print(name)
        print(f"  Win probability:            {result['win_probability']:.3f}")
        print(f"  Draw probability:           {result['draw_probability']:.3f}")
        print(f"  Loss probability:           {result['loss_probability']:.3f}")
        print(f"  Simulated expected points: {result['expected_points']: .3f}")
        print(f"  Theoretical expected pts:   {result['theoretical_expected_points']:.3f}")
        print(f"  Monte Carlo standard err:   {result['standard_error']:.4f}")
        print()

    difference = (
        results["Decision A"]["expected_points"]
        - results["Decision B"]["expected_points"]
    )

    theoretical_difference = (
        results["Decision A"]["theoretical_expected_points"]
        - results["Decision B"]["theoretical_expected_points"]
    )

    print(f"Estimated expected-points difference (A - B):   {difference:.3f}")
    print(f"Theoretical expected-points difference (A - B): {theoretical_difference:.3f}")


if __name__ == "__main__":
    main()

# SOLUTION:
# Simulations per decision: 100,000

# Decision A
#   Win probability:            0.349
#   Draw probability:           0.402
#   Loss probability:           0.250
#   Simulated expected points:  1.447
#   Theoretical expected pts:   1.450
#   Monte Carlo standard err:   0.0038

# Decision B
#   Win probability:            0.401
#   Draw probability:           0.319
#   Loss probability:           0.279
#   Simulated expected points:  1.524
#   Theoretical expected pts:   1.520
#   Monte Carlo standard err:   0.0040

# Estimated expected-points difference (A - B):   -0.076
# Theoretical expected-points difference (A - B): -0.070

