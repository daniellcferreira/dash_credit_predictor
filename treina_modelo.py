# Importa dataset do repositório UCI via ucimlrepo
from ucimlrepo import fetch_ucirepo
import joblib
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carrega o dataset "Heart Disease"
heart_disease = fetch_ucirepo(id=45)

# Seleciona os dados e cria a coluna alvo binária (1 = tem doença, 0 = não tem)
dados = heart_disease.data.features
dados["doenca"] = (heart_disease.data.targets > 0) * 1

# Separa features (X) e alvo (y)
X = dados.drop(columns='doenca')
y = dados['doenca']

# Divide em treino e teste com estratificação para manter proporção de classes
X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.2, random_state=432, stratify=y
)

# Treina o modelo com XGBoost
modelo = xgb.XGBClassifier(objective='binary:logistic')
modelo.fit(X_train, y_train)

# Realiza predições no conjunto de teste
y_pred = modelo.predict(X_test)

# Avalia acurácia do modelo
acuracia = accuracy_score(y_test, y_pred)
print(f'A acurácia do modelo é {acuracia:.2%}')

# Salva o modelo treinado
joblib.dump(modelo, 'modelo_xgboost.pkl')

# Salva as medianas das features (útil para preenchimento de valores faltantes)
medianas = X.median()
joblib.dump(medianas, 'medianas.pkl')
