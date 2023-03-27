import pandas as pd 
from dash import Dash
from dash import dcc
from dash import html 
from dash import Input, Output 
from  plotly import express as px

# get data 
df = pd.read_csv("data/sales.csv")
# get regions 
regions = list(df["Region"].unique())
# css styles 
styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# build  Dash app
app = Dash(__name__,external_stylesheets=styles)
# create a figure 
#fig= px.line(df, x="Date", y="Sales", title='Pink Morsal Sales')
app.layout = html.Div(
    children = [html.H1(children="Pink Morsel Sales over Time", id='header'),
                dcc.RadioItems(options=regions,value=regions[0], inline=True, id='region-radio'),
                dcc.Graph(id='selected-figure')
                
                ]
)


@app.callback(
    Output('selected-figure', 'figure'),
    Input('region-radio', 'value')
)
def update_figure(region):
    region_df = df[df["Region"] == region]

    fig = px.line(region_df, x="Date", y="Sales", hover_name="Region")

    fig.update_layout(title={
        'text': f"Sales of Pink Morsal in the {region}",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

    return fig

# run the app
if __name__ == '__main__':
    app.run_server(debug=True)