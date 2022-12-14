from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import pickle

app = Dash(__name__)

server = app.server

# Loading pickles
# notebook.fleury.io create pickle from final dataframe
df_transat = pickle.load(open('pickles/dataframe_transat.pickle', 'rb'))  # type: pd.DataFrame
df_transat_1h = pickle.load(open('pickles/dataframe_transat_1h.pickle', 'rb'))  # type: pd.DataFrame

globe_trace_plot = px.scatter_geo(
    df_transat,
    # title="Guadeloupe - France",
    # height=1000,
    lat='lat', lon='lon',
    color='speed',
    custom_data=['time'],
    hover_data={'time': True, 'speed': ':.2f', 'lat': ':.2f', 'lon': ':.2f'},
    labels={'lat': 'Lat', 'lon': 'Lon', 'speed': 'Speed', 'time': 'Time'},
    projection="orthographic") \
    .update_traces(marker_size=3) \
    .update_geos(
    # resolution=50,
    # fitbounds="locations",
    projection_rotation_lon=-45,
    projection_rotation_lat=30,
    showcoastlines=True, coastlinecolor="RebeccaPurple",
    showland=True, landcolor="LightGreen",
    showocean=True, oceancolor="LightBlue",
    showlakes=True, lakecolor="LightBlue",
    showrivers=True, rivercolor="LightBlue",
    lataxis_showgrid=True, lonaxis_showgrid=True,
    lataxis_dtick=90, lonaxis_dtick=180)\
    .update_layout(
    autosize=True,
    margin=dict(t=5, b=5, l=0, r=0)
    )

mapbox_trace_plot = px.scatter_mapbox(df_transat, lat='lat', lon='lon', color='speed',
                                      mapbox_style='open-street-map',
                                      custom_data=['time'],
                                      hover_data={'time': True, 'speed': ':.2f', 'lat': ':.2f', 'lon': ':.2f'},
                                      labels={'lat': 'Lat', 'lon': 'Lon', 'speed': 'Speed', 'time': 'Time'},
                                      zoom=2.5,
                                      )\
    .update_traces(marker_size=3.2)\
    .update_layout(
    autosize=True,
    margin=dict(t=5, b=5, l=0, r=0)
    )

app.title = 'North Transatlantic 2022'

app.layout = html.Div([
    html.H1('North Transatlantic 2022'),

    dcc.Tabs([
        dcc.Tab(label='Globe', children=[
            dcc.Graph(
                id='transat_plot_globe',
                figure=globe_trace_plot,
                style={'width': '100vw', 'height': '85vh'}
            )
        ]),
        dcc.Tab(label='Geo map', children=[
            dcc.Graph(
                id='trasat_plot_mapbox',
                figure=mapbox_trace_plot,
                style={'width': '100vw', 'height': '85vh'}
            )
        ]),
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
