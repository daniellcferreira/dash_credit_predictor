import pandas as pd
import pickle

# Caminho para o CSV baixado
df = pd.read_csv('data/german_credit_data.csv')

# Remove colunas irrelevantes
df = df.drop(columns=['Risk', 'CustomerId'], errors='ignore')

# Filtra apenas as colunas numéricas
df_numericas = df.select_dtypes(include=['int64', 'float64'])

# Calcula medianas
medianas = df_numericas.median()

# Salva em arquivo .pkl
with open('data/medianas.pkl', 'wb') as f:
  pickle.dump(medianas, f)

print("Medianas calculadas e salvas em 'data/medianas.pkl'")