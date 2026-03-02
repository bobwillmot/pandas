"""Generate and save a sample 50x10 pandas DataFrame."""

import pandas as pd


def create_sample_dataframe(rows: int = 50, columns: int = 10) -> pd.DataFrame:
    """Create a DataFrame with sequential integer values.

    Parameters
    ----------
    rows : int, default 50
        Number of rows to generate.
    columns : int, default 10
        Number of columns to generate.

    Returns
    -------
    pd.DataFrame
        Generated DataFrame with column names col_1 ... col_n.
    """
    data = {
        f"col_{index + 1}": list(range(1 + index, rows + 1 + index))
        for index in range(columns)
    }
    return pd.DataFrame(data)


def main() -> None:
    """Create a sample DataFrame and save it to CSV."""
    dataframe = create_sample_dataframe(rows=50, columns=10)
    dataframe.to_csv("sample.csv", index=False)
    print(dataframe)
    print("\nSaved to sample.csv")


if __name__ == "__main__":
    main()
