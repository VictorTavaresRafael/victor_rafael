# Readme da Sprint: Imersão em AWS

## Visão Geral do Projeto

Este documento resume as atividades e aprendizados adquiridos durante a sprint de estudos focada em Amazon Web Services (AWS), como parte do programa de bolsa. A sprint foi estruturada em quatro módulos principais, abrangendo desde os conceitos de negócio e valor da nuvem até a aplicação prática em laboratórios e um desafio de dados, culminando em uma experiência de aprendizado gamificada com o AWS Cloud Quest.

Para mim, que nunca havia tido contato com o universo da computação em nuvem, esta sprint foi uma jornada de descoberta imensa. Cada etapa contribuiu para construir uma base sólida de conhecimento, desmistificando o funcionamento da nuvem e suas aplicações práticas.

---

## Módulos da Sprint

### 1. AWS Partner: Sales Accreditation (Business)

O primeiro módulo foi uma introdução conceitual aos serviços da AWS sob uma perspectiva de negócios. O foco foi entender e saber comunicar a proposta de valor da nuvem, aprendendo a articular os benefícios para os clientes, lidar com objeções comuns e entender o modelo de vendas em parceria com a AWS. Adquiri ferramentas e modelos mentais essenciais para iniciar conversas eficazes sobre soluções em nuvem.

### 2. AWS Partner: Cloud Economics Accreditation

Aprofundando nos aspectos de negócio, este curso abordou a importância do gerenciamento financeiro na nuvem (Cloud Financial Management). O conteúdo focou em como auxiliar clientes a perceberem os benefícios econômicos da AWS, explorando os pilares do **AWS Cloud Value Framework** e as melhores práticas para otimização de custos e maximização de valor.

### 3. Laboratórios Práticos e Desafio AWS

Esta foi a etapa mais prática e desafiadora da sprint. O objetivo era aplicar os conhecimentos em um cenário real, utilizando diversos serviços da AWS.

**Laboratórios Realizados:**
* Lab AWS S3
* Lab AWS Athena
* Lab AWS Lambda
* Lab de Limpeza de Recursos

**Desafio de Dados:**

O desafio prático consolidou o aprendizado dos laboratórios e consistiu em um projeto de análise de dados de ponta a ponta:

* **Etapa 1: Preparação e Envio para a Nuvem**
    * Escolha de um conjunto de dados (`JSON` ou `CSV`) do portal de dados públicos do Governo Brasileiro.
    * Análise inicial do arquivo para definir 3 questionamentos de negócio.
    * Criação de um script em Python utilizando a biblioteca **`boto3`** para carregar o arquivo de dados em um bucket no **AWS S3**.

* **Etapa 2: Análise de Dados na Nuvem**
    * Desenvolvimento de um segundo script Python que lia o arquivo diretamente do bucket S3.
    * Utilização da biblioteca **`pandas`** para criar um DataFrame e realizar as análises propostas.
    * Aplicação obrigatória de manipulações específicas, como:
        * Filtros com múltiplos operadores lógicos.
        * Funções de agregação (ex: `sum()`, `mean()`, `count()`).
        * Funções condicionais (ex: `np.where`).
        * Funções de conversão de tipos de dados.
        * Funções para manipulação de datas e strings.

* **Etapa 3: Entrega dos Resultados**
    * Após as análises, o(s) arquivo(s) resultante(s) foi salvo de volta no mesmo bucket S3, mantendo o formato original.
    * Todo o processo foi realizado sem baixar o arquivo para a máquina local após o upload inicial, simulando um fluxo de trabalho real na nuvem.

As entregas incluíram os notebooks (`.ipynb`) com os códigos, este `README.md`, imagens de evidência da execução e os arquivos de dados resultantes.

### 4. AWS Cloud Quest: Cloud Practitioner

A última etapa da sprint foi, sem dúvida, a mais marcante. O **AWS Cloud Quest** é uma experiência de aprendizado baseada em RPG (Role-Playing Game) que transforma o estudo em uma jornada interativa. Como um iniciante no assunto, achei a didática simplesmente fantástica.

Através de 12 missões práticas e gratuitas, pude construir soluções do mundo real de forma guiada e divertida. A combinação de vídeos, diagramas, quizzes e, principalmente, a gamificação, tornou o aprendizado de conceitos fundamentais como **computação, redes, segurança e armazenamento** extremamente fluido e eficaz. A abordagem do "aprender fazendo" dentro de um jogo solidificou os conhecimentos teóricos e práticos de uma maneira muito mais poderosa do que os métodos tradicionais.

---

## Conclusão e Principais Aprendizados

Esta sprint foi fundamental para minha introdução à computação em nuvem. Saí do zero para uma compreensão prática sobre como os serviços da AWS funcionam e se conectam para resolver problemas reais. A combinação de teoria de negócios, prática em laboratorios e a didática inovadora do **Cloud Quest** proporcionou uma curva de aprendizado acelerada e muito gratificante. O desafio final me deu a confiança para manipular dados e automatizar processos na nuvem, uma habilidade essencial no mercado atual.