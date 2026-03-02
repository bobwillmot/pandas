"""Pytest tests for sample DataFrame generation."""

from pathlib import Path

import pandas as pd
import pytest

import sample


def test_create_sample_dataframe_shape_and_columns() -> None:
    """It creates a DataFrame with expected shape, columns, and dtypes."""
    dataframe = sample.create_sample_dataframe(rows=50, columns=10)

    assert dataframe.shape == (50, 10)
    assert list(dataframe.columns) == [
        "id",
        "score",
        "name",
        "is_active",
        "signup_date",
        "category",
        "ratio",
        "count_nullable",
        "tag",
        "priority",
    ]
    assert pd.api.types.is_integer_dtype(dataframe["id"])
    assert pd.api.types.is_float_dtype(dataframe["score"])
    assert pd.api.types.is_string_dtype(dataframe["name"])
    assert pd.api.types.is_bool_dtype(dataframe["is_active"])
    assert pd.api.types.is_datetime64_any_dtype(dataframe["signup_date"])
    assert pd.api.types.is_float_dtype(dataframe["ratio"])
    assert pd.api.types.is_integer_dtype(dataframe["count_nullable"])
    assert isinstance(dataframe["priority"].dtype, pd.CategoricalDtype)


def test_main_writes_sample_csv(monkeypatch: pytest.MonkeyPatch,
                                tmp_path: Path) -> None:
    """It writes a 50x10 CSV file when main is executed."""
    monkeypatch.chdir(tmp_path)

    sample.main()

    output_file = tmp_path / "sample.csv"
    assert output_file.exists()

    dataframe = pd.read_csv(output_file)
    assert dataframe.shape == (50, 10)
