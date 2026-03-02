"""Starter script for basic pandas DataFrame operations."""

import sys

import pandas as pd


def build_sample_dataframe() -> pd.DataFrame:
    """Build a sample DataFrame for quick local testing."""
    data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [30, 25, 35],
        "city": ["Seattle", "Austin", "Boston"],
    }
    return pd.DataFrame(data)


def ensure_supported_python() -> None:
    """Exit early when Python is lower than the project requirement."""
    minimum = (3, 14)
    if sys.version_info < minimum:
        version = f"{minimum[0]}.{minimum[1]}"
        raise SystemExit(f"Python {version}+ is required.")


if __name__ == "__main__":
    ensure_supported_python()
    df = build_sample_dataframe()
    print("Sample DataFrame:")
    print(df)
    print("\nSummary stats:")
    print(df.describe(include="all"))
