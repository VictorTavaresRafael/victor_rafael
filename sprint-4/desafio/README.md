# Desafio de Análise de Dados: Movimento Migratório no Brasil com Jupyter

Este projeto foi desenvolvido como parte de um desafio para um programa de bolsas. O objetivo é demonstrar um fluxo de trabalho de análise de dados, desde a limpeza até a geração de insights, utilizando Python, Pandas e Jupyter Notebooks.

## 📝 Descrição do Projeto

O projeto é dividido em duas etapas principais, representadas por dois Jupyter Notebooks:

1.  **`etl.ipynb` (Extração, Transformação e Limpeza):** Este notebook é responsável por carregar o conjunto de dados brutos (`STI_MOVIMENTO_2025_06.csv`), realizar a limpeza de colunas, tratar tipos de dados e, ao final, salvar uma versão limpa e processada do dataset.
2.  **`analise.ipynb` (Análise Exploratória):** Utilizando os dados já limpos pela etapa de ETL, este notebook foca em responder às perguntas de negócio, realizando análises e agrupamentos. Os insights gerados são salvos em arquivos `.csv` na pasta `resultados/`.

### Análises Realizadas:
* Total de pessoas movimentadas por nacionalidade (Top 20).
* Total de movimentos por Unidade Federativa (UF) de atendimento.
* Total de movimentos por tipo de classificação (ex: Visitante, Permanente).

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Bibliotecas:** `pandas`
* **Ambiente:** Jupyter Notebook

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para executar o projeto em seu ambiente local.

### **1. Pré-requisitos**
* Ter o Python e o Jupyter Notebook/Jupyter Lab instalados. Você pode instalar o Jupyter com `pip install notebook`.
* Ter clonado este repositório.

### **2. Instale as Dependências**
Abra o terminal na pasta do projeto, ative seu ambiente virtual (se estiver usando um) e instale a dependência:
```bash
pip install -r requirements.txt
```

### **3. Execute os Notebooks na Ordem Correta**
É crucial executar os notebooks na sequência correta, pois a análise depende dos dados limpos pelo ETL.

* **Passo 1: Execute `etl.ipynb`**
    * Abra o notebook `etl.ipynb` no Jupyter.
    * Clique em "Kernel" > "Restart & Run All" para executar todas as células.
    * Isso irá gerar o arquivo `dados_processados/movimento_migratorio_limpo.csv`.

* **Passo 2: Execute `analise.ipynb`**
    * Após a conclusão do primeiro notebook, abra `analise.ipynb`.
    * Execute todas as suas células ("Kernel" > "Restart & Run All").
    * Isso irá gerar os três relatórios de análise na pasta `resultados/`.

## 📂 Estrutura do Projeto
```
desafio-migracao/
├── dados/
│   └── STI_MOVIMENTO_2025_06.csv
├── dados_processados/
│   └── movimento_migratorio_limpo.csv
├── resultados/
│   ├── analise_nacionalidade.csv
│   ├── ...
├── .gitignore
├── analise.ipynb
├── etl.ipynb
├── README.md
└── requirements.txt
```