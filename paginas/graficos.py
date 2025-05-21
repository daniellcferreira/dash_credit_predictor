from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from ucimlrepo import fetch_ucirepo
import pandas as pd

# =========================
# Função para carregar os dados do UCI Repository
# =========================
def carregar_dados():
  """
  Carrega o dataset de doença cardíaca do UCI Repository.
  Retorna um DataFrame com as features e a coluna binária 'doenca'.
  """
  heart_disease = fetch_ucirepo(id=45)
  dados = heart_disease.data.features.copy()
  dados['doenca'] = (heart_disease.data.targets > 0).astype(int)
  return dados

# =========================
# Funções para criação dos gráficos
# =========================

def criar_histograma_idade(dados: pd.DataFrame):
  """
  Retorna um gráfico de histograma das idades.
  """
  fig = px.histogram(dados, x='age', title='Histograma de idades')
  return dcc.Graph(figure=fig)

def criar_boxplot_idade_por_doenca(dados: pd.DataFrame):
  """
  Retorna um boxplot das idades, separados por presença de doença.
  """
  fig = px.box(dados, x='doenca', y='age', color='doenca', title='Boxplot de idades por diagnóstico')
  return dcc.Graph(figure=fig)

# =========================
# Montagem do layout da página de gráficos
# =========================
def gerar_layout():
  """
  Retorna o layout HTML com os gráficos.
  """
  dados = carregar_dados()

  return html.Div([
    html.H1('Análise de dados do UCI Repository Heart Disease', className='text-center mb-5'),
    dbc.Container([
      dbc.Row([
        dbc.Col([
          html.H2('Histograma de idades'),
          criar_histograma_idade(dados)
        ], md=6),
        dbc.Col([
          html.H2('Boxplot de idades'),
          criar_boxplot_idade_por_doenca(dados)
        ], md=6)
      ])
    ])
  ])

# =========================
# Variável exportada usada pelo app.py
# =========================
layout = gerar_layout()
