# app.py

from dash import Dash
import dash_bootstrap_components as dbc

# Instância principal do aplicativo Dash
# - O tema FLATLY é aplicado via Bootstrap
# - O arquivo main.css é carregado depois para permitir sobreposições de estilo
# - suppress_callback_exceptions=True permite callbacks definidos em outras páginas
app = Dash(
  __name__,
  external_stylesheets=[dbc.themes.FLATLY, 'assets/main.css'],
  suppress_callback_exceptions=True
)
