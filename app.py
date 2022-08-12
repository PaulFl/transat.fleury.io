from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import pickle

app = Dash(__name__)

# Loading pickles
# notebook.fleury.io create pickle from final dataframe

globe_trace_plot = px.scatter_geo()


app.title = 'North Transatlantic 2022'

app.layout = html.Div([
    html.H1('North Transatlantic 2022'),

    dcc.Tabs([
        dcc.Tab(label='Globe', children=[
            dcc.Graph(
                id='transat_plot_globe',
                figure=globe_trace_plot
            )
        ]),
        dcc.Tab(label='Geo map'),
        dcc.Tab(label='Sat map'),
        dcc.Tab(label='Stats', children=[
            dcc.Markdown("""
                - Path
                    - Departure: Saint-Francois, Guadeloupe
                    - Horta, Azores
                    - Pornichet, France
                - Length
                    - Guadeloupe - Azores: 29 days
                    - Azores - France: 17 days
                    - Overall length: 46 days
                - Distance
                    - Straight line
                        - Guadeloupe - Azores: 
                        - Azores - France:
                        - Overall: 
                    - Total: 
                        - Guadeloupe - Azores: 
                        - Azores - France:
                        - Overall: 
                - Average speed:
                    - Straight line
                        - Guadeloupe - Azores: 
                        - Azores - France:
                        - Overall: 
                    - Total: 
                        - Guadeloupe - Azores: 
                        - Azores - France:
                        - Overall:
                
            """)
        ])
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)