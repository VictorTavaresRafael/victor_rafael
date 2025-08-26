# Desafio de Engenharia de Dados - Sprint 6: Da Camada Raw para a Trusted

## 1. Objetivo da Sprint
O objetivo central desta sprint foi processar os dados brutos e heterogêneos (CSV e JSON) da Camada Raw, aplicando um processo de ETL (Extração, Transformação e Carga) para criar uma **Camada Trusted**. O resultado final é um conjunto de dados limpo, padronizado, enriquecido e armazenado em um formato colunar otimizado (Parquet), pronto para as próximas etapas de análise e modelagem.

## 2. Arquitetura e Ferramentas
Para esta etapa, foi utilizada uma arquitetura serverless de processamento de dados na AWS:

* **Fonte de Dados:**
    * **AWS S3 (Camada Raw):** Contendo os arquivos CSV de filmes/séries e os arquivos JSON da API TMDB.
    * **AWS Glue Data Catalog:** As tabelas (`meubancodedados.local` e `meubancodedados.tmdb`), criadas por um Crawler do Glue, serviram como a fonte de metadados, desacoplando o script da localização física dos arquivos.

* **Ferramenta de ETL:**
    * **AWS Glue:** O serviço foi utilizado para executar um Job de ETL com um script em PySpark, processando os dados de forma distribuída e escalável.

* **Destino dos Dados:**
    * **AWS S3 (Camada Trusted):** A nova camada foi criada para armazenar os dados processados.
    * **Formato de Saída:** **Parquet**, escolhido por sua alta performance em consultas analíticas, compressão eficiente e integração com o ecossistema Spark e AWS.

## 3. Processo de Execução
O fluxo de trabalho para a construção da Camada Trusted foi o seguinte:

1.  **Descoberta de Schema (Crawler):** Primeiramente, um Crawler do AWS Glue foi executado sobre a Camada Raw para descobrir e catalogar automaticamente os schemas dos dados CSV e JSON, criando as tabelas no Data Catalog.

2.  **Desenvolvimento do Script ETL (PySpark):** Um script foi desenvolvido para o Glue Job, com a seguinte lógica:
    * **Extração:** O script inicia lendo os dados diretamente das tabelas no Glue Data Catalog, utilizando `glueContext.create_dynamic_frame.from_catalog()`.
    * **Transformação:** Uma série de transformações foram aplicadas para limpar e enriquecer os dados, incluindo:
        * Conversão de tipos de dados (ex: `string` para `integer` e `float`).
        * Tratamento de valores nulos (ex: `\N`).
        * Criação de uma coluna `tipo` para diferenciar "Movie" de "Series".
        * União dos datasets de filmes e séries.
        * Join com os dados da API para enriquecer o dataset final com informações de orçamento, popularidade e receita.
    * **Carga:** O DataFrame final e transformado foi salvo de volta no S3, no caminho da Camada Trusted, em formato Parquet e particionado pelas colunas `genero` e `tipo` para otimizar futuras consultas.

3.  **Execução do Glue Job:** O script foi configurado e executado como um Job formal no AWS Glue, garantindo um processo automatizável e monitorável.

## 4. Desafios Enfrentados e Soluções
Durante a execução, alguns desafios técnicos surgiram, exigindo depuração e ajustes no script:

* **Desafio 1: `EntityNotFoundException`**
    * **Problema:** O Job do Glue falhava ao iniciar, pois não conseguia encontrar as tabelas no Data Catalog.
    * **Solução:** A investigação revelou uma divergência entre os nomes de banco de dados e tabelas usados no script e os nomes exatos criados pelo Crawler.

* **Desafio 2: `DATATYPE_MISMATCH` (Erro de STRUCT)**
    * **Problema:** O Crawler, ao analisar os arquivos CSV, interpretou colunas com dados mistos (números e nulos) como um tipo de dado complexo (`STRUCT`), o que impedia a conversão direta para tipos numéricos.
    * **Solução:** O script PySpark foi adaptado para acessar os subcampos corretos dentro da `STRUCT` (ex: `col("anolancamento.long")` e `col("notamedia.string")`) antes de realizar a conversão, tratando o schema complexo de forma eficaz.

* **Desafio 3: `UNRESOLVED_COLUMN` (Erro de Digitação)**
    * **Problema:** Um erro de digitação no nome de uma coluna (`tituloprincipal` vs `titulopincipal`) impedia que o Spark resolvesse o schema do DataFrame.
    * **Solução:** Utilizando a própria sugestão na mensagem de erro do Spark, o nome da coluna no script foi corrigido, permitindo a execução bem-sucedida da transformação.

## 5. Evidências da Sprint 6

**Evidência 1: Execução do Glue Job com Sucesso**
*O print abaixo mostra o histórico de execução na aba "Runs" do AWS Glue, confirmando que o Job `ETL-Raw-Para-Trusted-v2` foi concluído com o status "Succeeded".*

(/sprint-6/evidencias/desafio/run-de-sucesso.png)

**Evidência 2: Estrutura da Camada Trusted no S3**
*O print abaixo evidencia a criação da nova camada no S3. É possível ver a pasta `Trusted/` e, dentro dela, os dados em formato Parquet, particionados por gênero e tipo, conforme definido no script ETL.*

[INSERIR AQUI O PRINT DO S3 MOSTRANDO A PASTA `Trusted/` COM AS PARTIÇÕES E ARQUIVOS PARQUET]

## 6. Conclusão da Sprint
A Sprint 6 foi concluída com sucesso. Os dados brutos foram processados, resultando em uma Camada Trusted limpa, padronizada, enriquecida e otimizada para performance. Este conjunto de dados agora serve como uma "fonte única da verdade" confiável, pronta para a etapa final de modelagem dimensional na Sprint 7.