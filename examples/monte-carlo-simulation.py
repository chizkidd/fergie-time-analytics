"""
Standalone Monte Carlo example.
A generic example showing how repeated simulations estimate outcome probabilities and 
expected points. Uses illustrative probabilities, not production Fergie Time parameters.

Demonstrates:
- Simulating win/draw/loss outcomes
- Estimating outcome probabilities
- Calculating expected points
- Quantifying Monte Carlo uncertainty

"""

import numpy as np


N_SIMULATIONS = 100_000
SEED = 42

# Illustrative outcome probabilities for two hypothetical decisions.
DECISIONS = {
    "Decision A": {"win": 0.35, "draw": 0.40, "loss": 0.25},
    "Decision B": {"win": 0.40, "draw": 0.32, "loss": 0.28},
}

POINTS = {
    "win": 3,
    "draw": 1,
    "loss": 0,
}


def simulate_decision(probabilities, n_simulations, rng):
    """Simulate outcomes and summarize their distribution."""
    outcomes = np.array(["win", "draw", "loss"])

    probabilities = np.array([
        probabilities["win"],
        probabilities["draw"],
        probabilities["loss"],
    ])

    if not np.isclose(probabilities.sum(), 1.0):
        raise ValueError("Outcome probabilities must sum to 1.")

    samples = rng.choice(
        outcomes,
        size=n_simulations,
        p=probabilities,
    )

    points = np.array([POINTS[outcome] for outcome in samples])

    mean_points = points.mean()
    standard_error = points.std(ddof=1) / np.sqrt(n_simulations)

    return {
        "win_probability": np.mean(samples == "win"),
        "draw_probability": np.mean(samples == "draw"),
        "loss_probability": np.mean(samples == "loss"),
        "expected_points": mean_points,
        "standard_error": standard_error,
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
        print(f"  Win probability:      {result['win_probability']:.3f}")
        print(f"  Draw probability:     {result['draw_probability']:.3f}")
        print(f"  Loss probability:     {result['loss_probability']:.3f}")
        print(f"  Expected points:      {result['expected_points']:.3f}")
        print(f"  Monte Carlo SE:       {result['standard_error']:.4f}")
        print()

    difference = (
        results["Decision A"]["expected_points"]
        - results["Decision B"]["expected_points"]
    )

    print(
        "Estimated expected-points difference "
        f"(A - B): {difference:.3f}"
    )


if __name__ == "__main__":
    main()