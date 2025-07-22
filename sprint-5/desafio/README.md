# Desafio Sprint 5 de Engenharia de Dados - Data Lake de Filmes

## 1. Objetivo do Projeto

Este projeto tem como objetivo a construção de um Data Lake ponta a ponta na nuvem AWS. O processo envolve a ingestão de dados de duas fontes distintas (arquivos CSV históricos e uma API de dados em tempo real), o armazenamento em diferentes camadas (Raw, Trusted, Refined), o processamento, a transformação e a modelagem dimensional dos dados, culminando na criação de dashboards analíticos para consumo final.

O escopo da análise será focado em filmes, explorando especificamente os gêneros **Crime** e **Guerra**.

## 2. Motivo da Análise (Questões de Negócio)

A análise busca extrair insights valiosos sobre o universo cinematográfico dos gêneros de Crime e Guerra. As seguintes questões de negócio foram definidas para guiar todo o processo de enriquecimento e modelagem dos dados:

1.  **Rentabilidade:** Qual a relação entre o orçamento de um filme e sua receita/popularidade? Filmes de Crime ou de Guerra possuem maior retorno sobre investimento (ROI)?
2.  **Desempenho de Elenco/Diretores:** Quais diretores ou atores estão mais associados a filmes de Crime e Guerra com altas avaliações tanto no IMDB quanto no TMDB? Existe uma nacionalidade de diretores que se destaca nesses gêneros?
3.  **Análise de Tendências:** Como a duração média dos filmes de Crime e Guerra mais populares mudou ao longo das décadas?
4.  **Análise de Plataformas e Sucesso:** Dentro dos gêneros de Crime e Guerra, qual plataforma (IMDB vs. TMDB) tem suas avaliações mais alinhadas ao sucesso financeiro (receita) do filme? Existem filmes clássicos do gênero que são aclamados pela crítica mas tiveram baixa receita?