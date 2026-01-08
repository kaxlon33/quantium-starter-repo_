import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("data/combined_sales_data.csv")

df['date'] = pd.to_datetime(df['date'])

df = df.sort_values('date')

daily_sales = (
    df.groupby('date', as_index=False)['Sales']
    .sum()
)

# -----------------------------
# Create line chart
# -----------------------------
fig = px.line(
    daily_sales,
    x='date',
    y='Sales',
    title='Pink Morsel Daily Sales Over Time',
    labels={
        'date': 'Date',
        'Sales': 'Total Daily Sales'
    }
)

fig.add_vline(
    x=pd.to_datetime("2021-01-15"),
    line_dash="dash",
    line_color="red"
)

app = dash.Dash(__name__)

app.layout = html.Div(
    style={'padding': '20px'},
    children=[
        html.H1("Pink Morsel Sales Visualiser"),
        html.P(
            "This chart shows total daily sales of Pink Morsels before and after "
            "the price increase on 15 January 2021."
        ),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
