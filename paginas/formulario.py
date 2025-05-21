from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import joblib
import pandas as pd
import numpy as np
from app import app

# Carregamento do modelo treinado e das medianas para imputação de valores nulos
modelo = joblib.load('modelo_xgboost.pkl')
medianas = joblib.load('medianas.pkl')

# Formulário interativo com campos de entrada
formulario = dbc.Container([
  html.P(
    "Preencha as informações abaixo e clique em prever para rodar o modelo",
    className="text-center mb-5"
  ),
  dbc.Row([
    dbc.Col([
      dbc.CardGroup([
        dbc.Label("Idade"),
        dbc.Input(id='idade', type='number', placeholder='Digite a idade'),
      ], className='mb-3'),

      dbc.CardGroup([
        dbc.Label("Sexo Biológico"),
        dbc.Select(id='sexo', options=[
          {'label': 'Masculino', 'value': '1'},
          {'label': 'Feminino', 'value': '0'}
        ]),
      ], className='mb-3'),

      dbc.CardGroup([
        dbc.Label("Tipo de dor no peito"),
        dbc.Select(id='cp', options=[
          {'label': 'Angina típica', 'value': '1'},
          {'label': 'Angina atípica', 'value': '2'},
          {'label': 'Não anginosa', 'value': '3'},
          {'label': 'Assintomática', 'value': '4'}
        ]),
      ], className='mb-3'),

      dbc.CardGroup([
        dbc.Label("Pressão arterial em repouso"),
        dbc.Input(id='trestbps', type='number', placeholder='Digite a pressão arterial'),
      ], className='mb-3'),

      dbc.CardGroup([
        dbc.Label("Colesterol sérico"),
        dbc.Input(id='chol', type='number', placeholder='Digite o colesterol sérico'),
      ], className='mb-3'),

      dbc.CardGroup([
        dbc.Label("Glicemia em jejum"),
        dbc.Select(id='fbs', options=[
          {'label': 'Menor que 120 mg/dl', 'value': '0'},
          {'label': 'Maior que 120 mg/dl', 'value': '1'}
        ]),
      ], className='mb-3'),

      dbc.CardGroup([
        dbc.Label("Eletrocardiograma em repouso"),
        dbc.Select(id='restecg', options=[
          {'label': 'Normal', 'value': '0'},
          {'label': 'Anormalidade ST-T', 'value': '1'},
          {'label': 'Hipertrofia ventricular esquerda', 'value': '2'}
        ]),
      ], className='mb-3'),
    ]),

    dbc.Col([
      dbc.CardGroup([
        dbc.Label("Frequência cardíaca máxima"),
        dbc.Input(id='thalach', type='number', placeholder='Digite a frequência máxima'),
      ], className='mb-3'),

      dbc.CardGroup([
        dbc.Label("Angina induzida por exercício"),
        dbc.Select(id='exang', options=[
          {'label': 'Sim', 'value': '1'},
          {'label': 'Não', 'value': '0'}
        ]),
      ], className='mb-3'),

      dbc.CardGroup([
        dbc.Label("Depressão do ST por exercício"),
        dbc.Input(id='oldpeak', type='number', placeholder='Digite o valor de oldpeak'),
      ], className='mb-3'),

      dbc.CardGroup([
        dbc.Label("Inclinação do segmento ST"),
        dbc.Select(id='slope', options=[
          {'label': 'Ascendente', 'value': '1'},
          {'label': 'Plana', 'value': '2'},
          {'label': 'Descendente', 'value': '3'}
        ]),
      ], className='mb-3'),

      dbc.CardGroup([
        dbc.Label("Nº de vasos principais coloridos por fluoroscopia"),
        dbc.Select(id='ca', options=[
          {'label': str(i), 'value': str(i)} for i in range(4)
        ]),
      ], className='mb-3'),

      dbc.CardGroup([
        dbc.Label("Cintilografia do miocárdio"),
        dbc.Select(id='thal', options=[
          {'label': 'Normal', 'value': '3'},
          {'label': 'Defeito fixo', 'value': '6'},
          {'label': 'Defeito reversível', 'value': '7'}
        ]),
      ], className='mb-3'),

      dbc.Button("Prever", id='botao-prever', color='success', n_clicks=0, className='mb-3 mt-3')
    ])
  ])
])

# Layout da página do formulário
layout = html.Div([
  html.H1("Previsão de Doença Cardíaca", className="text-center mt-5"),
  formulario,
  html.Div(id='previsao')
])

# Callback que processa os dados e exibe o resultado da previsão
@app.callback(
  Output('previsao', 'children'),
  [Input('botao-prever', 'n_clicks')],
  [State('idade', 'value'),
   State('sexo', 'value'),
   State('cp', 'value'),
   State('trestbps', 'value'),
   State('chol', 'value'),
   State('fbs', 'value'),
   State('restecg', 'value'),
   State('thalach', 'value'),
   State('exang', 'value'),
   State('oldpeak', 'value'),
   State('slope', 'value'),
   State('ca', 'value'),
   State('thal', 'value')]
)
def prever_doenca(n_clicks, idade, sexo, cp, trestbps, chol, fbs,
                  restecg, thalach, exang, oldpeak, slope, ca, thal):
  if n_clicks == 0:
    return ''

  # Criação do DataFrame com os dados do usuário
  entradas_usuario = pd.DataFrame(
    data=[[idade, sexo, cp, trestbps, chol, fbs, restecg,
           thalach, exang, oldpeak, slope, ca, thal]],
    columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
             'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
  )

  # Preenchimento de valores ausentes com as medianas
  entradas_usuario.fillna(medianas, inplace=True)

  # Conversão de tipos para garantir compatibilidade com o modelo
  entradas_usuario['oldpeak'] = entradas_usuario['oldpeak'].astype(np.float64)
  for col in entradas_usuario.columns:
    if col != 'oldpeak':
      entradas_usuario[col] = entradas_usuario[col].astype(np.int64)

  # Previsão com o modelo
  previsao = modelo.predict(entradas_usuario)[0]

  # Exibição da previsão ao usuário
  if previsao == 1:
    mensagem = "Você tem doença cardíaca"
    cor_do_alerta = 'danger'
  else:
    mensagem = "Você não tem doença cardíaca"
    cor_do_alerta = 'light'

  return dbc.Alert(mensagem, color=cor_do_alerta, className='d-flex justify-content-center mb-5')
