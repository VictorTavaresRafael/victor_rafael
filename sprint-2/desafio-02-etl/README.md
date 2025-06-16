# Desafio de ETL com Python Puro

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)

Um exercício de ETL (Extract, Transform, Load) para processar dados de um arquivo CSV utilizando apenas as funcionalidades nativas do Python, sem o uso de bibliotecas externas como Pandas.

## 📋 Sobre o Projeto

O objetivo deste desafio foi simular um processo de ETL para extrair, transformar e carregar dados sobre atores de Hollywood. A principal restrição era a proibição do uso de bibliotecas de manipulação de dados, o que exigiu a implementação de uma lógica de parsing e análise de forma manual.

O script `solucao_etl.py` realiza todo o processo e gera os arquivos de resultado na pasta `evidencias/`.

## ✅ Análises Realizadas (Etapas)

O script executa as 5 tarefas a seguir e salva cada resultado em um arquivo `.txt` separado:

1.  **Etapa 1:** Identifica o ator ou atriz com o maior número de filmes.
2.  **Etapa 2:** Calcula a média de receita bruta dos filmes de maior bilheteria de cada ator.
3.  **Etapa 3:** Identifica o ator ou atriz com a maior média de receita por filme.
4.  **Etapa 4:** Gera um ranking de frequência dos filmes de maior bilheteria.
5.  **Etapa 5:** Cria uma lista de todos os atores, ordenada de forma decrescente pela receita bruta total.

## ⚙️ Como Executar o Projeto

1.  Navegue até esta pasta no seu terminal.
2.  Execute o script Python:
    ```bash
    python solucao_etl.py
    ```
3.  Após a execução, os 5 arquivos de resultado (`etapa-1.txt` a `etapa-5.txt`) serão gerados ou atualizados dentro da pasta `evidencias/`.

## 🧠 Desafios e Aprendizados

* **Parsing Manual de CSV:** O maior desafio foi ler e separar os dados de um arquivo `.csv` sem o módulo `csv`, especialmente ao lidar com campos que continham vírgulas (como no nome "Robert Downey, Jr.").
* **Estruturação de Dados:** A escolha de usar uma lista de dicionários para armazenar os dados em memória foi crucial para facilitar as manipulações e análises subsequentes.
* **Algoritmos Fundamentais:** A implementação de lógicas de contagem de frequência e ordenação com múltiplos critérios utilizando apenas dicionários, listas e funções `lambda` reforçou conceitos essenciais de programação.

---

Feito por **Victor Tavares Rafael**.