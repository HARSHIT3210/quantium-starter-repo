import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, callback, html, dcc

# Load and sort the data
DATA_PATH = "./data/formatted_sales_data.csv"
data = pd.read_csv(DATA_PATH).sort_values(by="date")

# Initialize the Dash app with external stylesheet
app = Dash(__name__, external_stylesheets=[
    "https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.3.2/lux/bootstrap.min.css"  # Clean and modern Bootstrap theme
])

# Define layout
app.layout = html.Div(
    style={"padding": "2rem", "backgroundColor": "#f8f9fa", "minHeight": "100vh"},
    children=[
        html.H1(
            "Pink Morsel Visualizer",
            id="header",
            style={
                "textAlign": "center",
                "color": "#343a40",
                "marginBottom": "2rem",
                "fontWeight": "bold"
            }
        ),
        html.Div(
            style={"textAlign": "center","gap":"12px" ,"marginBottom": "2rem"},
            children=[
                dcc.RadioItems(
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "South", "value": "south"},
                        {"label": "East", "value": "east"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"},
                    ],
                    value="north",
                    id="controls-and-radio-item",
                    inline=True,
                    style={"fontSize": "18px"}
                )
            ]
        ),
        html.Div(
            dcc.Graph(id="visualization"),
            style={
                "boxShadow": "0 0 20px rgba(0,0,0,0.1)",
                "borderRadius": "10px",
                "backgroundColor": "white",
                "padding": "1rem"
            }
        )
    ]
)

# Callback to update graph based on region
@callback(
    Output("visualization", "figure"),
    Input("controls-and-radio-item", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["region"] == selected_region]

    fig = px.line(
        filtered_data,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {selected_region.capitalize()}",
        template="plotly_white"
    )
    fig.update_layout(margin={"l": 40, "r": 20, "t": 60, "b": 40})
    return fig

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
