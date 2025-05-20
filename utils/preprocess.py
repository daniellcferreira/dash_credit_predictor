import pickle

# Carrega medianas calculadas a partir do dataset de treino
with open('data/medianas.pkl', 'rb') as f:
  medianas = pickle.load(f)

# Constrói vetor de entrada baseado nas medianas
# Substitui apenas os campos alterados pelo usuário
def construir_vetor(dicionario_valores: dict) -> list:
  vetor = medianas.copy()
  for chave, valor in dicionario_valores.items():
    vetor[chave] = valor
  return vetor.tolist()