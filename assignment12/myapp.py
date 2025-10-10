from dash import Dash, dcc, html, Input, Output 
import plotly.express as px  
import plotly.data as pldata  

df = pldata.gapminder()

countries = df['country'].drop_duplicates()

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": c, "value": c} for c in countries],
        value="Canada"  
    ),
    dcc.Graph(id="gdp-growth")
])

@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(country_name):
    filtered_df = df[df["country"] == country_name]

    fig = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        title=f"GDP per Capita Growth in {country_name}"
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)
