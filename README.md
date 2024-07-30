# Titanic Streamlit Project

![Titanic](https://miro.medium.com/v2/resize:fit:1200/format:webp/1*7SX7D4FSxA4sQe_2h4xU2w.png)

## Descrição do Projeto

Este projeto é uma aplicação de análise de dados e aprendizado de máquina desenvolvida em Python usando o framework **Streamlit**. Ele explora o famoso dataset do Titanic, disponível no Kaggle, e permite que os usuários interajam com os dados para obter insights sobre o desastre do Titanic. A aplicação inclui visualizações de dados e uma previsão de sobrevivência usando um modelo de Regressão Logística.

## Objetivos

- Explorar e visualizar os dados do Titanic.
- Analisar padrões de sobrevivência.
- Implementar um modelo de aprendizado de máquina para prever a sobrevivência.
- Criar uma interface interativa usando Streamlit.

## Funcionalidades

- Visualização de dados interativa com gráficos de distribuição e taxas de sobrevivência.
- Previsão de sobrevivência baseada em características do passageiro, como classe, idade, gênero, etc.
- Interface amigável e fácil de usar para explorar o dataset.

## Requisitos do Sistema

- Python 3.7 ou superior
- Navegador web (para executar a aplicação Streamlit)

## Bibliotecas Utilizadas

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)

## Instalação

Siga estas etapas para configurar o projeto em seu ambiente local:

1. Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/seuusuario/titanic-streamlit.git
   cd titanic-streamlit
   ```

2. Crie um ambiente virtual:

   ```bash
   python -m venv env
   ```

3. Ative o ambiente virtual:

   - **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source env/bin/activate
     ```

4. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para iniciar a aplicação Streamlit, execute o seguinte comando no terminal:

```bash
streamlit run app.py
```

Isso abrirá a aplicação no seu navegador padrão, onde você poderá interagir com a análise do Titanic e prever a sobrevivência de passageiros com base nas entradas fornecidas.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
titanic-streamlit/
│
├── app.py              # Código principal da aplicação Streamlit
├── requirements.txt    # Arquivo de requisitos com as dependências do projeto
└── README.md           # Documentação do projeto
```

### `app.py`

Este arquivo contém o código da aplicação Streamlit, incluindo:

- **Carregamento e Exploração de Dados**: Carrega o dataset do Titanic e exibe algumas estatísticas descritivas e visualizações de gráficos.
  
- **Visualizações**: Cria gráficos para a distribuição de idades e a taxa de sobrevivência.
  
- **Modelo de Previsão**: Implementa um modelo de Regressão Logística para prever a sobrevivência dos passageiros.

- **Interface de Usuário**: Configura a interface do Streamlit, permitindo que os usuários interajam com os dados e façam previsões baseadas em suas entradas.

### `requirements.txt`

Este arquivo lista todas as dependências de pacotes Python necessárias para executar a aplicação. As dependências podem ser instaladas usando o `pip install -r requirements.txt`.

## Exemplo de Uso

Após iniciar a aplicação, você verá uma interface como a abaixo:

![Streamlit Interface](https://streamlit.io/images/brand/streamlit-mark-light.png)

1. **Exploração de Dados**:
   - Visualize as primeiras linhas do dataset.
   - Observe a distribuição de idade e a taxa de sobrevivência dos passageiros.

2. **Previsão de Sobrevivência**:
   - Insira os dados de um passageiro, como classe, sexo, idade, etc., no painel lateral.
   - O modelo irá prever se o passageiro sobreviverá ou não com base nas entradas fornecidas.

## Contribuição

Contribuições são bem-vindas! Se você deseja melhorar este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request com suas melhorias.

## License

Este projeto é licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

