import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

DATA_PATH = "data/combined_sales_data.csv"
df = pd.read_csv(DATA_PATH)
df['date'] = pd.to_datetime(df['date'])

app = Dash(__name__)

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "fontFamily": "Arial, sans-serif",
        "background": "linear-gradient(to bottom right, #fef3f8, #ffe5f0, #ffeaf2)",
        "padding": "40px"
    },
    children=[

        html.Div(
            style={"marginBottom": "40px", "textAlign": "center"},
            children=[
                html.H1(
                    "Pink Morsel Sales Dashboard",
                    style={
                        "fontSize": "3rem",
                        "fontWeight": "bold",
                        "color": "#d63384",
                        "marginBottom": "10px"
                    }
                ),
                html.P(
                    "Filter by region to explore sales",
                    style={"color": "#6b7280", "fontSize": "1.2rem"}
                )
            ]
        ),

        # Filter + Chart
        html.Div(
            style={"display": "grid", "gridTemplateColumns": "250px 1fr", "gap": "20px"},
            children=[

                # Region Filter
                html.Div(
                    style={
                        "background": "white",
                        "padding": "20px",
                        "borderRadius": "15px",
                        "boxShadow": "0 4px 12px rgba(0,0,0,0.1)"
                    },
                    children=[
                        html.Label(
                            "Select Region",
                            style={"fontWeight": "bold", "marginBottom": "10px", "display": "block", "fontSize": "1.2rem"}
                        ),
                        dcc.RadioItems(
                            id="region-selector",
                            options=[
                                {"label": "All", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"}
                            ],
                            value="all",
                            style={"display": "flex", "flexDirection": "column", "gap": "15px", "fontSize": "1.1rem"}
                        )
                    ]
                ),

                # Big Chart
                html.Div(
                    style={
                        "background": "white",
                        "padding": "30px",
                        "borderRadius": "15px",
                        "boxShadow": "0 4px 20px rgba(0,0,0,0.15)"
                    },
                    children=[
                        dcc.Graph(
                            id="sales-line-chart",
                            style={"height": "600px"}  
                        )
                    ]
                )
            ]
        ),

        # Footer / Region Info
        html.Div(
            id="footer",
            style={"textAlign": "center", "color": "#6b7280", "marginTop": "40px", "fontSize": "1.1rem"}
        )
    ]
)

@callback(
    Output("sales-line-chart", "figure"),
    Output("footer", "children"),
    Input("region-selector", "value")
)
def update_chart(selected_region):

    filtered = df if selected_region == "all" else df[df["region"] == selected_region]
    daily_sales = filtered.groupby("date", as_index=False)["Sales"].sum()

    # Create line chart
    fig = px.line(
        daily_sales,
        x="date",
        y="Sales",
        title="Daily Pink Morsel Sales"
    )
    fig.update_layout(title_x=0.5, margin=dict(l=40, r=40, t=60, b=40))

    footer_text = f"Showing data for {selected_region.capitalize()} region" if selected_region != "all" else "Showing data for all regions"

    return fig, footer_text

if __name__ == "__main__":
    app.run(debug=True)
