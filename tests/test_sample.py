"""Pytest tests for sample DataFrame generation."""

from pathlib import Path

import pandas as pd
import pytest

import sample


def test_create_sample_dataframe_shape_and_columns() -> None:
    """It creates a DataFrame with expected shape and column names."""
    dataframe = sample.create_sample_dataframe(rows=50, columns=10)

    assert dataframe.shape == (50, 10)
    assert list(dataframe.columns) == [
        "col_1",
        "col_2",
        "col_3",
        "col_4",
        "col_5",
        "col_6",
        "col_7",
        "col_8",
        "col_9",
        "col_10",
    ]


def test_main_writes_sample_csv(monkeypatch: pytest.MonkeyPatch,
                                tmp_path: Path) -> None:
    """It writes a 50x10 CSV file when main is executed."""
    monkeypatch.chdir(tmp_path)

    sample.main()

    output_file = tmp_path / "sample.csv"
    assert output_file.exists()

    dataframe = pd.read_csv(output_file)
    assert dataframe.shape == (50, 10)
