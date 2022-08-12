from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import pickle

app = Dash(__name__)

# Loading pickles
# notebook.fleury.io create pickle from final dataframe

globe_trace_plot = px.scatter_geo()

