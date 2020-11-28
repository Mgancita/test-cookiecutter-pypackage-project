"""Test module for test_cookiecutter_pypackage_project."""

from test_cookiecutter_pypackage_project import __author__, __email__, __version__


def test_project_info():
    """Test __author__ value."""
    assert __author__ == "Marco Gancitano"
    assert __email__ == "marco.gancitano@example.com"
    assert __version__ == "0.0.0"
