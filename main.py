from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import paginas              # Importa o pacote com as páginas do app
from app import app         # Instância principal do Dash definida em app.py

# Barra de navegação do topo com links
navegacao = dbc.NavbarSimple(
  children=[
    dbc.NavItem(dbc.NavLink("Gráficos", href="/graficos")),
    dbc.NavItem(dbc.NavLink("Formulário", href="/formulario")),
  ],
  brand="Dashboard",
  brand_href="/",
  color="primary",
  dark=True,
)

# Define o layout principal da aplicação
app.layout = html.Div([
  dcc.Location(id='url', refresh=False),  # Detecta mudanças na URL
  navegacao,
  html.Div(id='conteudo')                 # Aqui será renderizado o conteúdo da página selecionada
])

# Callback que decide qual página exibir com base na URL
@app.callback(
  Output('conteudo', 'children'),
  [Input('url', 'pathname')]
)
def mostrar_pagina(pathname):
  if pathname == '/formulario':
    return paginas.formulario.layout
  elif pathname == '/graficos':
    return paginas.graficos.layout
  else:
    return html.P('Página inicial')  # Padrão para "/"

# Executa o servidor apenas se o script for chamado diretamente
if __name__ == "__main__":
  app.run(debug=False, port=8080, host='0.0.0.0')
