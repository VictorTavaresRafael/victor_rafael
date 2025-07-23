# Desafio de Engenharia de Dados - Data Lake de Séries e Filmes

## 1. Objetivo do Projeto

Este projeto tem como objetivo a construção de um Data Lake ponta a ponta na nuvem AWS. O processo envolve a ingestão de dados de duas fontes distintas (arquivos CSV históricos e uma API de dados em tempo real), o armazenamento em diferentes camadas (Raw, Trusted, Refined), o processamento, a transformação e a modelagem dimensional dos dados, culminando na criação de dashboards analíticos para consumo final.

O escopo da análise será focado em séries de TV e filmes, explorando especificamente os gêneros **Crime** e **Guerra**.

## 2. Motivo da Análise (Questões de Negócio)

A análise busca extrair insights valiosos sobre o universo cinematográfico dos gêneros de Crime e Guerra. As seguintes questões de negócio foram definidas para guiar todo o processo de enriquecimento e modelagem dos dados:

1.  **Popularidade vs. Custo:** Qual a relação entre o orçamento (buscado na API) e a popularidade da obra (dados do CSV + API)?
2.  **Desempenho de Criadores e Elenco:** Quais criadores, diretores ou atores principais estão mais associados a obras de Crime e Guerra com altas avaliações tanto no IMDB (do CSV) quanto no TMDB (da API)?
3.  **Análise de Formato e Tendências:** Como a duração média (para filmes) ou o número de episódios por temporada (para séries) mudou ao longo dos anos?
4.  **Análise de Avaliações e Sucesso:** As avaliações do IMDB (do CSV) ou do TMDB (da API) são melhores preditores da longevidade ou do sucesso de uma obra?

---

## 3. Execução do Desafio

### **Etapa 1: Ingestão de Dados Históricos (Batch)**

Nesta primeira etapa, foi realizada a ingestão dos dados frios (`movies.csv` e `series.csv`) da origem local para a camada **Raw** do Data Lake no Amazon S3.

#### **Tecnologias Utilizadas:**
* **Python:** Para a criação do script de automação.
* **Boto3:** Biblioteca Python da AWS para interagir com o serviço S3.
* **Docker:** Para criar um ambiente isolado e portável para a execução do script de ingestão.

#### **Arquivos Desenvolvidos:**

* `ingestao_raw_camada.py`: Script Python que lê os nomes dos arquivos a serem processados, monta o caminho de destino no S3 de forma dinâmica (incluindo partição por ano/mês/dia) e realiza o upload.
* `Dockerfile`: Contém as instruções para construir a imagem Docker, instalando as dependências (`boto3`) e configurando o ambiente para executar o script Python.
* `requirements.txt`: Arquivo que lista as bibliotecas Python necessárias para o projeto.

#### **Execução e Evidências:**

O processo foi executado localmente através de um container Docker. O comando `docker run` foi configurado para:
1.  Utilizar um **Volume (`-v`)** para mapear a pasta local `dados_locais` (contendo os CSVs) para o diretório `/app/data` dentro do container. Isso permite que o container acesse os arquivos sem que eles façam parte da imagem.
2.  Passar as **credenciais da AWS** de forma segura como variáveis de ambiente (`-e`), que são lidas automaticamente pelo Boto3.

**Evidência 1: Sucesso na Execução do Container**

O print abaixo mostra o terminal após a execução do comando `docker run`, confirmando que os dois arquivos, `series.csv` e `movies.csv`, foram carregados com sucesso.

<img src="/sprint-5/desafio/evidencias/upload-concluido.png"/>

**Evidência 2: Arquivos na Camada Raw do S3**

O segundo print mostra o resultado no console da AWS. Os arquivos foram persistidos no bucket S3, seguindo o padrão de nomenclatura e a estrutura de pastas particionadas por data, como exigido pelo desafio.

<img src="/sprint-5/desafio/evidencias/bucket-filme.png"/>
<br>
<img src="/sprint-5/desafio/evidencias/bucket-serie.png"/>

---
