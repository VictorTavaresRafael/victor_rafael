# Desafio de Análise de Dados com Python e Docker

![Status](https://img.shields.io/badge/status-concluído-brightgreen)

Projeto desenvolvido como parte de um desafio de estágio, com o objetivo de demonstrar habilidades em análise de dados com Python e a containerização de uma aplicação de ponta a ponta utilizando Docker e Docker Compose.

## 📝 Objetivo do Projeto

O desafio consiste em criar uma pipeline de dados automatizada que:
1.  **Limpa e Transforma (ETL):** Lê um arquivo CSV bruto sobre as turnês de maior bilheteria de artistas femininas, realiza a limpeza, renomeia colunas e cria novas features (como ano de início e fim da turnê).
2.  **Analisa e Responde:** Utiliza o arquivo limpo para responder a uma série de perguntas de negócio, gerando como saída um arquivo de texto com as respostas e gráficos para visualização de dados.
3.  **Containeriza:** Empacota todo o processo em containers Docker, garantindo que a aplicação possa ser executada em qualquer ambiente de forma consistente e isolada.

## 🚀 Tecnologias Utilizadas

- **🐍 Python:** Linguagem principal para os scripts.
- **🐼 Pandas:** Biblioteca para manipulação e análise dos dados.
- **📊 Matplotlib & Seaborn:** Bibliotecas para a criação das visualizações gráficas.
- **🐳 Docker & Docker Compose:** Ferramentas para criação e orquestração dos containers.

## 📁 Estrutura de Pastas

O projeto foi organizado da seguinte forma para separar as responsabilidades:

desafio-docker/
├── data/
│   └── concert_tours_by_women.csv     # Dado de entrada (bruto)
├── etl/
│   ├── etl.py                         # Script de extração, transformação e carga (ETL)
│   └── Dockerfile                     # Define como construir a imagem do ETL
├── job/
│   ├── job.py                         # Script de análise e geração das saídas
│   └── Dockerfile                     # Define como construir a imagem do Job
├── volume/                            # Volume compartilhado com os resultados
│   ├── csv_limpo.csv                  # Saída do ETL, entrada para o Job
│   ├── respostas.txt                  # Respostas das perguntas 1, 2 e 3
│   ├── Q4.png                         # Gráfico da pergunta 4
│   └── Q5.png                         # Gráfico da pergunta 5
├── docker-compose.yml                 # Orquestrador dos containers
└── README.md                          # Documentação do projeto

## ✨ Funcionalidades e Entregáveis

O script `job.py` processa os dados para responder às seguintes perguntas:

1.  Qual é a artista que mais aparece na lista e possui a maior média de faturamento bruto?
2.  Das turnês que aconteceram dentro de um ano, qual a turnê com a maior média de faturamento bruto?
3.  Quais são as 3 turnês com o show (unitário) mais lucrativo?
4.  **Gráfico de Linhas:** Mostra o faturamento por ano da turnê para a artista com mais aparições e maior somatório de faturamento.
5.  **Gráfico de Colunas:** Demonstra as 5 artistas com mais shows na lista.

## ⚙️ Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## ▶️ Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/victor-rafael/desafio-docker.git](https://github.com/victor-rafael/desafio-docker.git)
    ```
    *(Substitua pelo link do seu repositório)*

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd desafio-docker
    ```

3.  **Adicione o arquivo de dados:**
    Garanta que o arquivo `concert_tours_by_women.csv` esteja dentro da pasta `data/`.

4.  **Execute a aplicação com Docker Compose:**
    Este comando irá construir as imagens e iniciar os containers na ordem correta.
    ```bash
    docker-compose up --build
    ```

5.  **Verifique os resultados:**
    Após a execução, a pasta `volume/` conterá todos os arquivos de saída gerados pela pipeline.

## 🔄 Como Funciona a Orquestração?

Ao executar o `docker-compose up`:
1.  O serviço **`etl`** é iniciado primeiro. Ele lê o CSV da pasta `/data`, executa o script `etl.py` para limpar os dados e salva o `csv_limpo.csv` no volume compartilhado. Ao terminar, ele sai com código 0 (sucesso).
2.  Graças à diretiva `depends_on`, o serviço **`job`** só é iniciado após o `etl` ter sido concluído com sucesso.
3.  O `job` lê o `csv_limpo.csv` do mesmo volume compartilhado, executa o script `job.py` para fazer a análise e gera os arquivos `respostas.txt`, `Q4.png` e `Q5.png` nesse mesmo volume.

## Autor

Feito por **Victor Rafael**

