"""Generate and save a sample 50x10 pandas DataFrame."""

import pandas as pd


def create_sample_dataframe(rows: int = 50, columns: int = 10) -> pd.DataFrame:
    """Create a mixed-type sample DataFrame.

    Parameters
    ----------
    rows : int, default 50
        Number of rows to generate.
    columns : int, default 10
        Number of columns to generate.

    Returns
    -------
    pd.DataFrame
        Generated DataFrame with mixed datatypes.
    """
    signup_dates = pd.date_range(start="2025-01-01", periods=rows, freq="D")
    categories = ["A", "B", "C"]
    priorities = ["low", "medium", "high"]

    data = {
        "id": list(range(1, rows + 1)),
        "score": [round(50.0 + (index * 0.5), 2) for index in range(rows)],
        "name": [f"user_{index + 1:03d}" for index in range(rows)],
        "is_active": [index % 2 == 0 for index in range(rows)],
        "signup_date": signup_dates,
        "category": [categories[index % 3] for index in range(rows)],
        "ratio": [
            None if index % 10 == 0 else round(index / (rows - 1), 3)
            for index in range(rows)
        ],
        "count_nullable": pd.array(
            [None if index % 7 == 0 else index for index in range(rows)],
            dtype="Int64",
        ),
        "tag": [None if index % 5 == 0 else f"tag_{index % 4}"
                for index in range(rows)],
        "priority": pd.Categorical(
            [priorities[index % 3] for index in range(rows)],
            categories=priorities,
            ordered=True,
        ),
    }

    if columns < len(data):
        selected_columns = list(data.keys())[:columns]
        data = {column: data[column] for column in selected_columns}
    elif columns > len(data):
        for index in range(len(data) + 1, columns + 1):
            data[f"extra_{index}"] = list(range(rows))

    return pd.DataFrame(data)


def main() -> None:
    """Create a sample DataFrame and save it to CSV."""
    dataframe = create_sample_dataframe(rows=50, columns=10)
    dataframe.to_csv("sample.csv", index=False)
    print(dataframe)
    print("\nSaved to sample.csv")


if __name__ == "__main__":
    main()
