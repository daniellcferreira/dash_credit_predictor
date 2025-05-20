import pandas as pd
import pickle
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Carrega o dataset
df = pd.read_csv('data/german_credit_data.csv')

# Trata variáveis categóricas com Label Encoding
for coluna in df.select_dtypes(include=['object']).columns:
  df[coluna] = LabelEncoder().fit_transform(df[coluna])

# Define variáveis independentes(X) e dependentes(y)
X = df.drop(columns=['Risk'])
y = df['Risk']

# Divide o conjunto em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Cria e treina o modelo XGBoost
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X_train, y_train)

# Salva o modelo treinado em formato .pkl
with open('model/modelo.pkl', 'wb') as f:
  pickle.dump(model, f)

print("Modelo treinado e salvo em 'model/modelo.pkl'")
