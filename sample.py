"""Generate and save a sample 50x10 pandas DataFrame."""

from pathlib import Path
import webbrowser

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


def export_paginated_html(
        dataframe: pd.DataFrame,
        output_path: Path,
        rows_per_page: int = 10,
) -> None:
        """Export DataFrame to HTML with client-side pagination controls."""
        table_html = dataframe.to_html(index=False, table_id="data-table")

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Sample DataFrame</title>
</head>
<body>
    <h1>Sample DataFrame</h1>
    <div id="table-container">{table_html}</div>
    <div id="pagination-controls">
        <label for="rows-per-page">Rows per page:</label>
        <select id="rows-per-page">
            <option value="5">5</option>
            <option value="10">10</option>
            <option value="25">25</option>
            <option value="50">50</option>
        </select>
        <span id="row-count-info"></span>
        <button id="prev-page" type="button">Previous</button>
        <span id="page-info"></span>
        <button id="next-page" type="button">Next</button>
    </div>
    <script>
        (function () {{
            const table = document.getElementById("data-table");
            const bodyRows = Array.from(table.querySelectorAll("tbody tr"));
            const rowsPerPageSelect = document.getElementById("rows-per-page");
            const prevButton = document.getElementById("prev-page");
            const nextButton = document.getElementById("next-page");
            const pageInfo = document.getElementById("page-info");
            const rowCountInfo = document.getElementById("row-count-info");
            let currentPage = 1;
            let currentRowsPerPage = {rows_per_page};

            rowsPerPageSelect.value = String(currentRowsPerPage);

            function getTotalPages() {{
                return Math.max(1, Math.ceil(bodyRows.length / currentRowsPerPage));
            }}

            function renderPage(page) {{
                const totalPages = getTotalPages();
                currentPage = page;
                const start = (currentPage - 1) * currentRowsPerPage;
                const end = start + currentRowsPerPage;
                bodyRows.forEach((row, index) => {{
                    row.style.display = index >= start && index < end ? "" : "none";
                }});
                pageInfo.textContent = `Page ${{currentPage}} of ${{totalPages}}`;
                rowCountInfo.textContent = `Total rows: ${{bodyRows.length}}`;
                prevButton.disabled = currentPage === 1;
                nextButton.disabled = currentPage === totalPages;
            }}

            prevButton.addEventListener("click", () => {{
                if (currentPage > 1) {{
                    renderPage(currentPage - 1);
                }}
            }});

            nextButton.addEventListener("click", () => {{
                const totalPages = getTotalPages();
                if (currentPage < totalPages) {{
                    renderPage(currentPage + 1);
                }}
            }});

            rowsPerPageSelect.addEventListener("change", (event) => {{
                currentRowsPerPage = Number(event.target.value);
                renderPage(1);
            }});

            renderPage(1);
        }})();
    </script>
</body>
</html>
"""

        output_path.write_text(html_content, encoding="utf-8")


def main() -> None:
    """Create a sample DataFrame and save it to CSV and HTML."""
    dataframe = create_sample_dataframe(rows=50, columns=10)
    dataframe.to_csv("sample.csv", index=False)
    html_path = Path("sample.html")
    export_paginated_html(dataframe, html_path)

    print(dataframe)
    print("\nSaved to sample.csv")
    print(f"Saved to {html_path}")

    webbrowser.open(html_path.resolve().as_uri())


if __name__ == "__main__":
    main()
