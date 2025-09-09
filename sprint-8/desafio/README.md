# Desafio de Engenharia de Dados - Sprint 8: Camada de Consumo com AWS QuickSight

## 1. Objetivo da Sprint
O objetivo da Sprint 8, a fase final do projeto, foi construir a **Camada de Consumo** do Data Lake. Esta etapa consistiu em utilizar uma ferramenta de Business Intelligence (BI) para se conectar aos dados já limpos e modelados na Camada Refined, a fim de criar um dashboard analítico e interativo que respondesse às questões de negócio definidas no início do desafio.

## 2. Arquitetura e Ferramentas
Para a camada de consumo, a seguinte arquitetura serverless foi implementada, garantindo performance e escalabilidade:

* **Fonte de Dados:**
    * **AWS S3 (Camada Refined):** Armazenamento dos dados finais em formato Parquet, organizados em um modelo dimensional (Esquema Estrela) com as tabelas `dim_obras` e `fato_metricas_obras`.
    * **AWS Glue Data Catalog:** O catálogo de metadados foi essencial, contendo as definições das tabelas da camada Refined, permitindo que outros serviços as encontrassem e entendessem seus schemas.

* **Motor de Consulta (Query Engine):**
    * **AWS Athena:** Utilizado como uma ponte entre o QuickSight e os dados no S3. O Athena permite executar consultas SQL padrão diretamente nos arquivos Parquet, usando os metadados do Glue Data Catalog, sem a necessidade de carregar os dados para um banco de dados tradicional.

* **Ferramenta de Visualização (BI):**
    * **AWS QuickSight:** A ferramenta de BI da AWS foi usada para se conectar ao Athena, criar um conjunto de dados (dataset) e construir os visuais do dashboard final. A utilização do motor **SPICE** do QuickSight foi escolhida para garantir alta performance e interatividade nos painéis.

## 3. Processo de Execução
O fluxo de trabalho para a construção do dashboard foi o seguinte:

1.  **Catalogar a Camada Refined:** Um Crawler do AWS Glue (`Crawler-Refined`) foi executado sobre a pasta `s3://.../Refined/` para descobrir e catalogar as tabelas `dim_obras` e `fato_metricas_obras`, tornando-as visíveis para outros serviços como o Athena.

2.  **Configurar o QuickSight:** Foram ajustadas as permissões de segurança no painel de administração do QuickSight para garantir que o serviço tivesse autorização para acessar o AWS Athena e o bucket S3 do projeto.

3.  **Criar o Dataset:** Dentro do QuickSight, um novo dataset foi criado utilizando o **Athena** como fonte. As tabelas `dim_obras` e `fato_metricas_obras` foram selecionadas e unidas (join) através da chave substituta (`obra_sk`), recriando o nosso modelo estrela dentro do ambiente de análise.

4.  **Construir a Análise:** Com o dataset pronto, os visuais foram construídos na tela de "Analysis", arrastando e soltando os campos para criar gráficos que respondessem diretamente a cada uma das questões de negócio. Foram adicionados filtros interativos para permitir uma exploração mais aprofundada dos dados.

## 4. Resultado Final e Evidências
O resultado final é um dashboard completo e funcional que transforma os dados processados em insights claros e acionáveis.

**Evidência 1: Dashboard Analítico Final**
*O print abaixo mostra a visão geral do dashboard construído no QuickSight. Ele inclui os KPIs principais, os filtros interativos e os gráficos que consolidam as respostas para as questões de negócio.*

<img src="/sprint-8/evidencias/desafio/dashbord-completo.png"/>

**Evidência 2: Gráficos Respondendo às Questões de Negócio**
*Os prints a seguir detalham cada visualização criada, mostrando como elas respondem às perguntas que guiaram o projeto.*

* **Análise de Popularidade (Pergunta 1):**
    <img src="/sprint-8/evidencias/desafio/grafico--notas-por-tipo.png"/>

* **Análise de Tendências (Pergunta 3):**
<img src="/sprint-8/evidencias/desafio/grafico-ano-lancamento.png"/>

* **Análise Comparativa de Avaliações (Pergunta 4):**
<img src="/sprint-8/evidencias/desafio/grafico-notas-por-genero.png"/>

## 5. Conclusão da Sprint
A Sprint 8 concluiu com sucesso o ciclo de vida dos dados no projeto. Todo o pipeline de engenharia, desde a ingestão de dados brutos até a modelagem na camada Refined, culminou na criação de um produto de dados tangível e de alto valor: um dashboard analítico. Esta etapa demonstrou a capacidade de consumir os dados processados e traduzi-los em inteligência de negócio, finalizando o desafio de ponta a ponta.