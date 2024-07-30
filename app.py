import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Análise do Titanic",  # Define o título da aba do navegador
    layout="centered",                # Layout da página (pode ser 'centered' ou 'wide')
    initial_sidebar_state="expanded"  # Estado inicial da barra lateral (pode ser 'expanded' ou 'collapsed')
)

# Função para carregar os dados do Titanic
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    return pd.read_csv(url)

# Carregar os dados
data = load_data()

# Configuração da página
st.title("Análise do Dataset Titanic")
st.sidebar.title("Exploração de Dados")
st.sidebar.markdown("Este é um projeto de análise de dados do Titanic.")

# Exploração de dados
st.header("Visualização dos Dados")
st.write(data.head())

# Gráfico da distribuição de idades usando Streamlit
def plot_age_distribution(data):
    st.subheader("Distribuição de Idades")
    st.bar_chart(data['Age'].value_counts().sort_index())

# Gráfico da taxa de sobrevivência usando Streamlit
def plot_survival_rate(data):
    st.subheader("Taxa de Sobrevivência")
    survival_counts = data['Survived'].value_counts()
    survival_df = pd.DataFrame({'Survived': survival_counts.index, 'Count': survival_counts.values})
    st.bar_chart(survival_df.set_index('Survived'))

# Gráficos
plot_age_distribution(data)
plot_survival_rate(data)

# Modelo de Machine Learning
st.sidebar.subheader("Previsão de Sobrevivência")
pclass = st.sidebar.selectbox("Classe do Passageiro", [1, 2, 3], index=0)
sex = st.sidebar.selectbox("Sexo", ["male", "female"], index=0)
age = st.sidebar.slider("Idade", int(data['Age'].min()), int(data['Age'].max()), int(data['Age'].median()))
sibsp = st.sidebar.slider("Número de Irmãos/Cônjuges a Bordo", 0, 8, 0)
parch = st.sidebar.slider("Número de Pais/Filhos a Bordo", 0, 6, 0)
fare = st.sidebar.slider("Tarifa", float(data['Fare'].min()), float(data['Fare'].max()), float(data['Fare'].median()))
embarked = st.sidebar.selectbox("Porto de Embarque", ["C", "Q", "S"], index=0)

# Seleção de features e target
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
X = data[features]
y = data['Survived']

# Pré-processamento: converter variáveis categóricas em numéricas
X = pd.get_dummies(X, drop_first=True)

# Tratamento de valores nulos
X['Age'].fillna(X['Age'].median(), inplace=True)
X['Fare'].fillna(X['Fare'].median(), inplace=True)

# Divisão dos dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Construção do modelo
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Converter entrada do usuário para DataFrame
input_data = pd.DataFrame({
    'Pclass': [pclass],
    'Sex': [sex],
    'Age': [age],
    'SibSp': [sibsp],
    'Parch': [parch],
    'Fare': [fare],
    'Embarked': [embarked]
})

# Pré-processar entrada do usuário
input_data = pd.get_dummies(input_data, drop_first=True)
input_data['Age'].fillna(X['Age'].median(), inplace=True)
input_data['Fare'].fillna(X['Fare'].median(), inplace=True)

# Ajuste para garantir que as colunas no input_data sejam as mesmas que no X
missing_cols = set(X.columns) - set(input_data.columns)
for col in missing_cols:
    input_data[col] = 0
input_data = input_data[X.columns]

# Prever sobrevivência
survival_prediction = model.predict(input_data)[0]
survival_prob = model.predict_proba(input_data)[0][1]

st.sidebar.subheader("Resultado da Previsão")
if survival_prediction == 1:
    st.sidebar.write(f"**O passageiro provavelmente sobreviverá. Probabilidade: {survival_prob:.2f}**")
else:
    st.sidebar.write(f"**O passageiro provavelmente não sobreviverá. Probabilidade: {survival_prob:.2f}**")
