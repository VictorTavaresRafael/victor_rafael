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
<br>

### Etapa 2: Ingestão de Dados da API (Streaming)

A segunda etapa do projeto focou em enriquecer os dados existentes. O objetivo foi utilizar os IDs das obras (`imdb_id`) presentes nos arquivos CSV para consultar uma API externa (TMDB - The Movie Database), obter dados complementares (como orçamento, receita, popularidade) e salvar essas novas informações como arquivos JSON na camada Raw do Data Lake.

#### **Tecnologias Utilizadas:**
* **AWS Lambda:** Para a execução do código de forma serverless.
* **AWS S3:** Como fonte dos dados originais e destino para os novos dados JSON.
* **AWS IAM:** Para o gerenciamento de permissões de acesso da função Lambda.
* **Python:** Com as bibliotecas `boto3` (para interagir com a AWS), `pandas` (para manipulação de dados) e `requests` (para as chamadas de API).
* **Docker:** Utilizado de forma crucial para construir um pacote de dependências (Layer) compatível com o ambiente da Lambda.

#### **Arquivos Desenvolvidos:**

* `lambda_function.py`: O código central da função Lambda. Foi desenvolvido para ser robusto, incluindo:
    * Leitura dinâmica do S3 para encontrar os arquivos CSV mais recentes, sem depender de datas fixas.
    * Processamento de arquivos grandes em "chunks" para evitar estouro de memória.
    * Chamadas à API do TMDB para enriquecimento dos dados.
    * Tratamento de erros e escrita do resultado final em formato JSON de volta ao S3, em um caminho particionado por data.

#### **Desafios Enfrentados e Soluções**

Esta etapa apresentou desafios técnicos significativos, que são comuns em projetos de engenharia de dados no mundo real.

* **Desafio 1: Incompatibilidade de Ambiente (Windows vs. Linux)**
    * **Problema:** A função Lambda falhava ao tentar importar a biblioteca `pandas`, retornando o erro `AttributeError: module 'os' has no attribute 'add_dll_directory'`. Isso ocorreu porque as dependências, quando instaladas localmente no Windows, não são compatíveis com o ambiente Linux da AWS Lambda.
    * **Solução:** A solução foi criar um pacote de dependências (Lambda Layer) em um ambiente Linux simulado. Para isso, utilizamos um **container Docker** com a imagem `python:3.9` para executar o `pip install`. Em uma segunda etapa, devido a um problema de montagem de volume, utilizamos o comando `docker cp` para copiar os pacotes já instalados de dentro do container para a máquina local, garantindo 100% de compatibilidade.

* **Desafio 2: Estouro de Memória (`Runtime.OutOfMemory`)**
    * **Problema:** Mesmo após corrigir o Layer, a função falhava por exceder a memória alocada (mesmo com 1 GB). Isso acontecia porque o arquivo `movies.csv` era muito grande para ser carregado na memória de uma só vez pelo `pandas`.
    * **Solução:** O código foi refatorado para usar uma abordagem de processamento em _streaming_. Utilizando o parâmetro `chunksize` da função `pandas.read_csv`, o arquivo foi lido em pedaços de 100.000 linhas por vez. Isso permitiu extrair os IDs necessários mantendo o uso de memória baixo e controlado (reduzindo de >1GB para ~316MB).

#### **Execução e Evidências:**

A função Lambda foi finalmente executada com sucesso após a implementação das otimizações de código e da correção do Layer de dependências.

**Evidência 3: Sucesso na Execução da Lambda Otimizada**

O print abaixo mostra o log da execução bem-sucedida no AWS CloudWatch, onde a função processa os arquivos em _chunks_ e conclui a coleta.

<img src="/sprint-5/desafio/evidencias/execucao-lambda.png"/>

**Evidência 4: Arquivo JSON Enriquecido na Camada Raw**

Finalmente, o print a seguir mostra o resultado no S3: a criação da pasta `Raw/TMDB/` e o arquivo JSON contendo os dados coletados da API, salvo com sucesso no bucket.

<img src="/sprint-5/desafio/evidencias/pasta-tmdb-json.png"/>

## 4. Conclusão

Este desafio representou uma jornada completa e prática na construção das fundações de um Data Lake na nuvem AWS. Ao final desta etapa, o objetivo principal de criar uma **Camada Raw** funcional e populada com dados de múltiplas fontes foi alcançado com sucesso.

### Principais Conquistas e Aprendizados:

* **Arquitetura Híbrida de Ingestão:** Foi implementado um pipeline capaz de lidar tanto com a ingestão de dados em **batch**, a partir de arquivos CSV legados usando Docker, quanto com a coleta de dados de uma **API externa** em tempo real através de uma arquitetura serverless com AWS Lambda.

* **Resolução de Desafios Técnicos Reais:** O projeto serviu como uma arena para solucionar problemas complexos e comuns no dia a dia de um engenheiro de dados:
    * **Compatibilidade de Ambientes:** O desafio de empacotar dependências Python (Layers) para o ambiente Linux da Lambda, mesmo desenvolvendo em Windows, reforçou a importância do **Docker** como ferramenta essencial para garantir a portabilidade e consistência entre ambientes.
    * **Otimização de Memória:** O confronto com erros de `OutOfMemory` ao processar arquivos grandes foi um aprendizado crucial, levando à implementação de técnicas de **processamento em streaming (chunks)**, uma habilidade indispensável para lidar com Big Data.

* **Orquestração de Serviços AWS:** O projeto integrou com sucesso um conjunto de serviços essenciais da AWS (S3, Lambda, IAM), demonstrando a capacidade de construir soluções de dados robustas e escaláveis na nuvem.

### Próximos Passos

Com a Camada Raw estabelecida, o projeto está pronto para avançar para as próximas fases:

1.  **Sprint 6 (Camada Trusted):** Utilizar o **AWS Glue** para executar jobs de ETL que irão ler os dados brutos, limpá-los, transformá-los e salvá-los em formato Parquet, criando uma fonte de dados confiável e otimizada.
2.  **Sprint 7 (Camada Refined):** Aplicar uma modelagem dimensional sobre os dados da camada Trusted, preparando-os para análises de negócio.
3.  **Sprint 8 (Camada de Consumo):** Conectar o **AWS QuickSight** à camada Refined para construir dashboards e responder às questões de negócio definidas no início do desafio.
---
