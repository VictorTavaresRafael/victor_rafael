# Resumo da Sprint 3 de Desenvolvimento - [Junho/2025]

## Visão Geral

Esta sprint foi focada na capacitação e aprofundamento em três pilares fundamentais da tecnologia moderna: **Containerização com Docker**, **Computação em Nuvem com a AWS** e **Manipulação Avançada de Dados com Python e REGEX**. O objetivo foi adquirir tanto conhecimentos teóricos aprofundados quanto experiência prática através de um desafio de ponta a ponta.

---

## Focos de Aprendizado

### 1. Docker para Desenvolvedores (com Docker Swarm e Kubernetes)

Curso intensivo focado na criação, gerenciamento e orquestração de containers, cobrindo desde os fundamentos até tópicos avançados de produção.

**Principais Tópicos Abordados:**
- **Criação de Imagens:** Boas práticas para escrever `Dockerfile` eficientes e otimizados.
- **Gerenciamento de Dados:** Uso de `Volumes` para persistência de dados.
- **Redes:** Comunicação entre containers e exposição de portas.
- **Orquestração Multi-Container:** Automação de ambientes complexos com `Docker Compose`.
- **Orquestração em Cluster:** Introdução aos conceitos de orquestração em escala com **Docker Swarm** (nativo) e **Kubernetes (K8s)** (padrão de mercado), entendendo como gerenciar aplicações distribuídas e resilientes.

### 2. AWS Partner: Accreditation (Technical)

Capacitação com foco técnico e comercial para parceiros AWS, visando não apenas o entendimento dos serviços, mas também a habilidade de comunicar seu valor de negócio aos clientes.

**Principais Tópicos Abordados:**
- **Proposta de Valor da AWS:** Entendimento dos benefícios da nuvem, como agilidade, elasticidade, economia e alcance global.
- **Fundamentos dos Serviços:** Conceitos básicos dos principais serviços da AWS (EC2, S3, RDS, VPC, etc.).
- **Comunicação Eficaz:** Como articular o valor de negócio da nuvem e lidar com objeções comuns de clientes.
- **Modelo de Parceria:** Estratégias para vender e construir soluções em conjunto com a AWS.

- [Certificado](https://www.credly.com/badges/fde28331-8179-46a1-8d94-37956e703496/linked_in?t=syooj0)

### 3. Guia Prático de REGEX com Python

Estudo focado no uso de Expressões Regulares (REGEX), uma ferramenta poderosa para busca, validação e extração de padrões em textos.

**Principais Tópicos Abordados:**
- **Sintaxe e Metacaracteres:** Entendimento dos blocos de construção de uma expressão regular.
- **Módulo `re` do Python:** Aplicação prática utilizando as funções `search()`, `match()`, `findall()` e `sub()`.
- **Casos de Uso:** Utilização de REGEX para limpeza de dados (data cleaning), validação de formatos (e-mails, telefones) e extração de informações específicas de grandes volumes de texto.

---

## Desafio Prático: Pipeline de Dados com Docker

Para aplicar e solidificar os conhecimentos, foi desenvolvido um desafio prático de análise de dados. O projeto consistiu na criação de uma **pipeline de dados em dois estágios (ETL e Job de Análise), totalmente orquestrada com Docker Compose.**

- **Etapa 1 (ETL):** Um container foi responsável por ler um dataset bruto, realizar a limpeza, renomear colunas e transformar dados (como extrair anos de uma string usando REGEX).
- **Etapa 2 (Job):** Um segundo container, executado em sequência, consumiu os dados limpos para realizar análises com Pandas, gerando um arquivo de texto com respostas e gráficos como saída.

Este projeto prático foi crucial para consolidar os conceitos de `Dockerfile`, `Docker Compose`, `Volumes` e a comunicação entre containers em um cenário real.

---

## Principais Competências Desenvolvidas

- **Containers e Orquestração:** Habilidade de criar, gerenciar e orquestrar aplicações com Docker e Docker Compose, com entendimento conceitual de Swarm e Kubernetes.
- **Cloud Computing (AWS):** Visão abrangente sobre o ecossistema AWS, combinando conhecimento técnico fundamental com a capacidade de comunicar seu valor de negócio.
- **Análise e Manipulação de Dados:** Aprofundamento em Python e Pandas, com a adição da habilidade de usar REGEX para tarefas complexas de limpeza e extração de dados.
- **Cultura DevOps:** Entendimento prático de como a containerização facilita a criação de ambientes de desenvolvimento e produção consistentes e automatizados.
