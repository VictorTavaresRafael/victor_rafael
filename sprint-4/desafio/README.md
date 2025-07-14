# Desafio de Análise de Dados e Integração com AWS S3

Este projeto foi desenvolvido como parte de um desafio para um programa de bolsas. O objetivo é demonstrar um fluxo de trabalho completo de análise de dados, desde a limpeza até o upload seguro dos resultados para a nuvem da AWS.

## 📝 Descrição do Projeto

O projeto utiliza um conjunto de dados sobre movimentos migratórios no Brasil e é dividido em duas etapas principais, representadas por dois Jupyter Notebooks:

1.  **`etl.ipynb` (Extração, Transformação e Limpeza):** Responsável por carregar os dados brutos, realizar a limpeza e prepará-los para a análise, salvando uma versão processada.
2.  **`analise.ipynb` (Análise e Upload para AWS):** Carrega os dados limpos, realiza as análises principais e, como passo final, faz o upload dos relatórios gerados para um bucket no Amazon S3.

### Análises Realizadas
O notebook de análise busca responder às seguintes perguntas-chave sobre o fluxo migratório:

* **Análise por Nacionalidade:** Qual o ranking das 20 nacionalidades com maior volume de entradas e saídas no país?
* **Análise por UF:** Como a movimentação de pessoas se distribui entre os postos de fronteira das diferentes Unidades Federativas (UF)?
* **Análise por Classificação:** Qual o volume de movimentos para cada tipo de classificação (ex: Visitante, Permanente, Temporário)?

### 🔐 Boas Práticas de Segurança
A integração com a AWS segue as melhores práticas de segurança. As credenciais de acesso são gerenciadas fora do código, em um arquivo `.env` (ignorado pelo Git), e carregadas dinamicamente usando a biblioteca `python-dotenv`.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Bibliotecas:** `pandas`, `boto3`, `python-dotenv`
* **Ambiente:** Jupyter Notebook
* **Cloud:** Amazon Web Services (AWS) S3

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para executar o projeto.

### 1. Pré-requisitos
* Python e Jupyter Notebook instalados.
* Uma conta na AWS com credenciais de acesso e um bucket S3 criado.

### 2. Configure o Ambiente
* Clone este repositório.
* Crie e ative um ambiente virtual.
* Instale as dependências: `pip install -r requirements.txt`

### 3. Configure as Credenciais da AWS
* Crie um arquivo chamado `.env` na raiz do projeto.
* Adicione suas credenciais e o nome do bucket neste formato:
    ```ini
    AWS_ACCESS_KEY_ID="SUA_CHAVE_DE_ACESSO"
    AWS_SECRET_ACCESS_KEY="SUA_CHAVE_SECRETA"
    AWS_S3_BUCKET="NOME_DO_SEU_BUCKET"
    ```

### 4. Execute os Notebooks na Ordem Correta
1.  **Execute `etl.ipynb` primeiro:** Abra e execute todas as células para gerar os dados limpos.
2.  **Execute `analise.ipynb` em seguida:** Abra e execute todas as células para realizar as análises e enviar os resultados para o S3.

### 5. Verifique os Resultados
* Acesse o seu bucket no console da AWS S3 para confirmar que os 3 arquivos de análise foram carregados com sucesso.