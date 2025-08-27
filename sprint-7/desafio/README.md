### Etapa 4: Modelagem Dimensional (Trusted -> Camada Refined)

Esta sprint representa a fase final do processo de ETL, onde os dados limpos da camada Trusted foram reorganizados em um modelo dimensional otimizado para análises de BI e consultas complexas. O resultado é a criação da **Camada Refined**.

* **Processo:** Utilizando novamente um Job do AWS Glue com PySpark, os dados em Parquet da camada Trusted foram lidos e transformados em um **Esquema Estrela (Star Schema)**. Este modelo consiste em:
    * **Tabela Fato (`fato_metricas_obras`):** Uma tabela central contendo chaves e todas as métricas quantitativas (notas, votos, orçamento, receita, popularidade).
    * **Tabela Dimensão (`dim_obras`):** Uma tabela contendo os atributos descritivos e contextuais de cada filme e série (título, ano, gênero, etc.).
    Para conectar as duas tabelas, uma chave substituta (Surrogate Key) numérica e única, `obra_sk`, foi gerada e adicionada a ambas.

* **Desafios e Soluções:**
    * **Problema: `TypeError: 'Column' object is not callable`:** O principal desafio foi um erro de sintaxe persistente e sutil no PySpark. Mesmo com o código parecendo correto, o job falhava repetidamente.
    * **Solução:** A causa raiz foi identificada como a complexidade de uma única instrução encadeada. A solução foi **refatorar o código**, quebrando a criação da tabela fato em múltiplos passos explícitos: primeiro, a seleção das colunas; segundo, o tratamento de valores nulos; e por último, a renomeação. Essa abordagem não só resolveu o erro, mas também tornou o código mais legível e de fácil manutenção.

* **Evidências:**
    * **Execução do Glue Job com Sucesso:**
        *O print abaixo mostra o histórico de execução no AWS Glue, confirmando que o Job `ProcessaTrustedParaRefined` foi concluído com o status "Succeeded".*

        <img src="/sprint-7/evidencias/desafio/run-de-sucesso.png"/>

    * **Estrutura da Camada Refined no S3:**
        *Este print evidencia a criação da nova camada no S3. É possível ver a pasta `Refined/` e, dentro dela, as duas tabelas do nosso modelo dimensional: `dim_obras` e `fato_metricas_obras`, ambas salvas em Parquet.*

        <img src="/sprint-7/evidencias/desafio/camada-refined-enriquecida.png"/>

---