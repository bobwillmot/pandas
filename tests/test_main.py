"""Unit tests for the starter pandas script."""

import unittest
from unittest.mock import patch

import src.main as main


class TestPythonVersionGuard(unittest.TestCase):
    """Tests for Python version requirement checks."""

    def test_ensure_supported_python_allows_314(self) -> None:
        """It should pass for Python 3.14 and newer."""
        with patch.object(main.sys, "version_info", (3, 14, 0)):
            main.ensure_supported_python()

    def test_ensure_supported_python_rejects_313(self) -> None:
        """It should exit when Python is below 3.14."""
        with patch.object(main.sys, "version_info", (3, 13, 12)):
            with self.assertRaises(SystemExit) as error:
                main.ensure_supported_python()

        self.assertEqual(str(error.exception), "Python 3.14+ is required.")


if __name__ == "__main__":
    unittest.main()
