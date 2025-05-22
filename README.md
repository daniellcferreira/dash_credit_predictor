# Heart Dash IA

![Python](https://img.shields.io/badge/Python-Linguagem%20de%20Programação-blue?style=flat-square&logo=python&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-Framework%20de%20Dashboards-009BDE?style=flat-square&logo=plotly&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Gráficos%20Interativos-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![UCI ML Repo](https://img.shields.io/badge/UCI%20ML%20Repo-Fonte%20de%20Dados-brown?style=flat-square&logo=databricks&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-Modelo%20de%20Machine%20Learning-darkgreen?style=flat-square&logo=xgboost&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Manipulação%20de%20Dados-black?style=flat-square&logo=pandas&logoColor=white)
![Dash Bootstrap Components](https://img.shields.io/badge/Bootstrap-Componentes%20Responsivos-563D7C?style=flat-square&logo=bootstrap&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-Estilização%20da%20Interface-264de4?style=flat-square&logo=css3&logoColor=white)

---

## Descrição

Este projeto consiste em uma aplicação web interativa construída com a biblioteca **Dash**, voltada para visualização e análise de dados sobre doenças cardíacas extraídos do **UCI Machine Learning Repository**. O objetivo principal é proporcionar uma interface clara, funcional e responsiva que permita ao usuário explorar características dos dados e entender a distribuição e impacto de variáveis como idade, presença de doença e outros indicadores clínicos.

Além disso, o projeto também apresenta um formulário simples para simular a predição de risco de crédito utilizando um modelo de machine learning previamente treinado com **XGBoost**, demonstrando como integrar visualizações e análises com modelos reais de inferência.

A aplicação está estruturada com navegação de páginas, separação modular dos componentes, uso de estilos personalizados via CSS e adoção de boas práticas de organização e legibilidade de código, mantendo a escalabilidade e manutenibilidade do projeto.

---

## Funcionalidade

- Visualização de histograma de idades com base nos dados clínicos.
- Exibição de boxplot das idades segmentadas pela presença de doença cardíaca.
- Simulação de formulário para entrada de dados e predição de risco.
- Navegação entre páginas através de rotas definidas no Dash.
- Integração com dataset oficial do UCI ML Repository.
- Interface responsiva com suporte a Bootstrap via `dash-bootstrap-components`.
- Aplicação de CSS customizado para melhoria visual.
- Organização em múltiplos arquivos e módulos (`paginas`, `assets`, etc.).
- Inclusão de alertas, gráficos interativos e layout responsivo por colunas.
- Separação clara entre lógica de interface, estilo e processamento de dados.
- Uso de modelo XGBoost previamente salvo e carregado via `pickle`.
- Compatibilidade com execução local e em redes privadas (host `0.0.0.0`).
- Carregamento de datasets e features com uso de bibliotecas modernas (`pandas`, `ucimlrepo`).
- Estrutura modular para facilitar a expansão do projeto com novos gráficos ou modelos.

---

## Tecnologias Abordadas

**Python 3.11**  
Linguagem principal do projeto, utilizada para toda a lógica de backend e definição da interface com o Dash.

**Dash**  
Framework principal de desenvolvimento da interface web interativa. Permite a construção de dashboards com Python puro e componentes do React.js por baixo dos panos.

**Dash Bootstrap Components**  
Biblioteca complementar ao Dash que fornece componentes pré-estilizados usando o framework Bootstrap 5, facilitando a criação de layouts responsivos e organizados.

**Plotly**  
Biblioteca de visualização de dados utilizada para construir gráficos interativos como histogramas e boxplots, totalmente integrados com Dash.

**Pandas**  
Biblioteca essencial para manipulação e análise de dados tabulares. Usada para ler, transformar e preparar os dados antes de exibição nos gráficos ou envio ao modelo.

**XGBoost**  
Framework de aprendizado de máquina usado para o modelo de predição de risco de crédito. O modelo foi treinado externamente e serializado com `pickle`.

**UCI ML Repository**  
Fonte de dados original do projeto, especificamente o conjunto sobre doenças cardíacas (id 45), carregado automaticamente com `ucimlrepo`.

**CSS3**  
Utilizado para aplicar estilos personalizados via o arquivo `assets/main.css`, ajustando margens, espaçamentos e características visuais da aplicação.

**Estrutura Modular**  
Separação de páginas (`graficos.py`, `formulario.py`), pasta de assets para CSS e arquitetura voltada para manutenibilidade e organização.

---
