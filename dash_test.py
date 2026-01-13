import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def app():
    return import_app("app")


def test_header_present(dash_duo, app):
    dash_duo.start_server(app)

    header = dash_duo.wait_for_element("#header", timeout=10)
    assert "Pink Morsel Sales Dashboard" in header.text


def test_visualisation_present(dash_duo, app):
    dash_duo.start_server(app)

    graph = dash_duo.wait_for_element('[id="sales-line-chart"]', timeout=10)
    assert graph is not None


def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)

    picker = dash_duo.wait_for_element("#region-selector", timeout=10)
    assert picker is not None
