# Desafio Sprint 5 de Engenharia de Dados - Data Lake de Séries

## 1. Objetivo do Projeto

Este projeto tem como objetivo a construção de um Data Lake ponta a ponta na nuvem AWS. O processo envolve a ingestão de dados de duas fontes distintas (um arquivo CSV histórico e uma API de dados em tempo real), o armazenamento em diferentes camadas (Raw, Trusted, Refined), o processamento, a transformação e a modelagem dimensional dos dados, culminando na criação de dashboards analíticos para consumo final.

O escopo da análise será focado em séries de TV, explorando especificamente os gêneros **Crime** e **Guerra**.

## 2. Motivo da Análise (Questões de Negócio)

A análise busca extrair insights valiosos sobre o universo das séries de TV dos gêneros de Crime e Guerra. As seguintes questões de negócio foram definidas para guiar todo o processo de enriquecimento e modelagem dos dados:

1.  **Popularidade vs. Custo:** Qual a relação entre o orçamento por episódio (buscado na API) e a popularidade da série (dados do CSV + API)? Séries de Crime ou de Guerra conseguem manter sua popularidade por mais temporadas?
2.  **Desempenho de Criadores e Elenco:** Quais criadores (showrunners) ou atores principais estão mais associados a séries de Crime e Guerra com altas avaliações tanto no IMDB (do CSV) quanto no TMDB (da API)? Existe uma nacionalidade de criadores que se destaca nesses gêneros?
3.  **Análise de Formato e Tendências:** Como o número de episódios por temporada em séries de Crime e Guerra mudou ao longo dos anos? Existe uma tendência para temporadas mais curtas ou mais longas?
4.  **Análise de Avaliações e Longevidade:** Dentro dos gêneros de Crime e Guerra, as avaliações do IMDB (do CSV) ou do TMDB (da API) são melhores preditores da longevidade de uma série (número de temporadas)? Existem séries aclamadas pela crítica que foram canceladas precocemente?