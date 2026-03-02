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
    """It writes CSV/HTML outputs and opens the HTML file in browser."""
    monkeypatch.chdir(tmp_path)

    opened_urls = []

    def fake_open(url: str) -> bool:
        opened_urls.append(url)
        return True

    monkeypatch.setattr(sample.webbrowser, "open", fake_open)

    sample.main()

    csv_file = tmp_path / "sample.csv"
    html_file = tmp_path / "sample.html"

    assert csv_file.exists()
    assert html_file.exists()
    assert opened_urls == [html_file.resolve().as_uri()]

    dataframe = pd.read_csv(csv_file)
    assert dataframe.shape == (50, 10)

    html_content = html_file.read_text(encoding="utf-8")
    assert "<table" in html_content
    assert 'id="pagination-controls"' in html_content
    assert 'id="rows-per-page"' in html_content
    assert 'id="row-count-info"' in html_content
    assert "Rows per page:" in html_content
    assert 'id="prev-page"' in html_content
    assert 'id="next-page"' in html_content
    assert "Page ${currentPage} of ${totalPages}" in html_content
    assert "Total rows: ${bodyRows.length}" in html_content
