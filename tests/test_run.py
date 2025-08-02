import pytest
from dash import Dash
from app import app  # Make sure app.py exposes `app` at the top level

# This is a built-in Dash testing fixture provided by dash[testing]
def test_app_starts(dash_duo):
    dash_duo.start_server(app)

    # Check if the title is rendered
    assert dash_duo.find_element("#header").text == "PINK MORSEL VISUALIZER"

    # Check if the default radio value is "north"
    radio = dash_duo.find_element("#controls-and-radio-item input:checked")
    assert radio.get_attribute("value") == "north"

    # Check if the graph loads
    graph = dash_duo.find_element("#visualization")
    assert graph is not None

    # Simulate clicking on 'south'
    dash_duo.select_dcc_radio_item("#controls-and-radio-item", "south")

    # Wait for the graph to update
    dash_duo.wait_for_text_to_equal(
        "#visualization .js-plotly-plot .gtitle", "Pink Morsel Sales - South", timeout=5
    )
