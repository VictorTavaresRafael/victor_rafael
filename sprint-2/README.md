# Sprint 2: Imersão em Python e Análise de Dados

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.x-blue.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-blue.svg)

## 📖 Visão Geral da Sprint

Esta sprint de duas semanas representou uma imersão completa no ecossistema Python, com foco em sua aplicação para a análise de dados. A jornada foi estruturada para construir uma base teórica sólida na primeira semana e, na segunda, aplicar intensivamente esses conhecimentos em exercícios práticos e em um projeto de maior escopo.

---

### **Semana 1: Fundamentos e Ferramentas**

A primeira semana foi dedicada ao aprendizado teórico e à familiarização com as ferramentas essenciais do analista de dados. As atividades incluíram:

* **Curso Intensivo de Python:** Uma carga horária de 14 horas cobrindo desde a sintaxe básica até conceitos mais avançados da linguagem.
* **Curso de Ciência de Dados:** Introdução às principais bibliotecas do ecossistema, como **Pandas** para manipulação de dados e **Matplotlib** para visualização.

Os [**certificados de conclusão**](./certificados/) destes cursos estão disponíveis como evidência do aprendizado teórico adquirido.

---

### **Semana 2: Prática e Desafio**

Com a base teórica estabelecida, a segunda semana foi focada na aplicação prática dos conhecimentos.

#### **Exercícios Práticos**

Para solidificar os conceitos, resolvi uma série de exercícios práticos, que estão organizados em seções. Cada seção contém um notebook com os desafios e suas respectivas soluções.

* ➡️ **[Acesse os notebooks de exercícios aqui.](./exercicios/)**

#### **Desafio da Sprint: Análise de Dados da Play Store**

O primeiro grande projeto da sprint foi uma análise completa de dados utilizando o dataset da Google Play Store e a biblioteca Pandas. O desafio envolveu um ciclo de ponta a ponta:

1.  **Carregamento e Limpeza:** Tratamento de dados duplicados, corrompidos e normalização de colunas.
2.  **Análise Exploratória:** Cálculo de indicadores chave para responder a perguntas específicas.
3.  **Visualização de Dados:** Criação de múltiplos gráficos para apresentar os insights de forma profissional.

* ➡️ **[Acesse o projeto completo do desafio.](./desafio-01-play-store/)**
* ➡️ **[Veja o notebook com toda a análise.](./desafio-01-play-store/desafio.ipynb)**

#### **Desafio Adicional: ETL com Python Puro (Seção 6)**

Para aprofundar os fundamentos de manipulação de arquivos e estruturas de dados, a Seção 6 apresentou um desafio de ETL (Extract, Transform, Load) utilizando **Python puro**, sem o auxílio de bibliotecas como Pandas ou CSV.

O projeto consistiu em:
1.  **Extrair** dados do arquivo `actors.csv` manualmente.
2.  **Transformar** os dados em memória, realizando 5 análises distintas (ex: ator com mais filmes, contagem de frequência, ordenação por receita).
3.  **Carregar** (Load) os resultados de cada análise em arquivos de texto separados.

Este exercício foi crucial para entender o funcionamento interno das grandes bibliotecas de dados e reforçar a lógica de programação fundamental.

* ➡️ **[Acesse o script da solução aqui.](./desafio-02-etl/solucao_etl.ipynb)**
* ➡️ **[Consulte os arquivos de resultado gerados.](./desafio-02-etl/resultados/)**

---

## 📂 Estrutura do Repositório da Sprint

* `certificados/`
    * *Armazena os certificados de conclusão dos cursos da Semana 1.*
* `desafio-01-play-store/`
    * *Contém o projeto de Análise da Play Store, com o notebook e evidências.*
* `exercicios/`
    * *Pasta com os notebooks e scripts de exercícios práticos.*
    * `secao-3/`
    * `secao-4/`
    * `secao-5/`
    * `secao-6/`
        * *Contém o desafio de ETL com Python puro.*
        * `solucao_etl.py`
        * `resultados/` (com os arquivos `etapa-X.txt`)
    * `...`
* `README.md`
    * *Este arquivo, que resume toda a jornada e os aprendizados da sprint.*

## ✅ Conclusão

Esta sprint foi uma jornada de grande aprendizado, permitindo-me ir da teoria à prática de forma estruturada. Sinto-me agora muito mais confiante para utilizar tanto as bibliotecas de alto nível quanto as funcionalidades nativas do Python para resolver problemas de dados do mundo real.