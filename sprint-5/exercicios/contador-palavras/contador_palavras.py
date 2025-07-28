# -*- coding: utf-8 -*-

"""
contador_palavras.py

Script PySpark para contar a frequência de palavras em um arquivo de texto.

Uso:
spark-submit contador_palavras.py <caminho_do_arquivo_de_entrada> <caminho_do_diretorio_de_saida>
"""

import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, lower, col

def main():
    """
    Função principal que executa o job Spark.
    """
    # 1. Validação dos argumentos de linha de comando
    if len(sys.argv) != 3:
        print("Erro: Número incorreto de argumentos.")
        print("Uso: spark-submit contador_palavras.py <arquivo_de_entrada> <diretorio_de_saida>")
        sys.exit(-1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # 2. Inicialização da SparkSession
    # A SparkSession é o ponto de entrada para qualquer funcionalidade do Spark.
    spark = SparkSession \
        .builder \
        .appName("ContadorDePalavras") \
        .getOrCreate()

    # 3. Leitura dos dados de entrada
    # Lê o arquivo de texto, criando um DataFrame com uma coluna "value"
    # onde cada linha do arquivo é uma linha no DataFrame.
    df_linhas = spark.read.text(input_path)

    # 4. Transformação dos dados
    # - Transforma todo o texto para minúsculas (lower) para contagem case-insensitive.
    # - Divide cada linha (coluna "value") em uma lista de palavras (split).
    # - Usa a função "explode" para que cada palavra da lista se torne uma nova linha
    #   em uma nova coluna chamada "palavra".
    df_palavras = df_linhas.select(explode(split(lower(col("value")), " ")).alias("palavra"))

    # 5. Contagem das palavras
    # - Filtra quaisquer linhas que possam estar vazias após o split.
    # - Agrupa os dados pela coluna "palavra".
    # - Conta as ocorrências em cada grupo.
    df_contagem = df_palavras.filter(col("palavra") != "") \
                             .groupBy("palavra") \
                             .count()

    # 6. Ordenação e formatação do resultado
    # - Renomeia a coluna "count" para "ocorrencias" para maior clareza.
    # - Ordena os resultados em ordem decrescente de ocorrências.
    df_resultado = df_contagem.withColumnRenamed("count", "ocorrencias") \
                              .orderBy(col("ocorrencias").desc())

    # 7. Exibição e salvamento do resultado
    print("Amostra do resultado:")
    df_resultado.show()

    print(f"Salvando resultado em: {output_path}")
    # O modo "overwrite" apaga o diretório de saída se ele já existir.
    # coalesce(1) junta os resultados em um único arquivo de saída (part-*.csv).
    df_resultado.coalesce(1).write.csv(output_path, header=True, mode="overwrite")

    # 8. Finalização da sessão Spark
    spark.stop()

if __name__ == "__main__":
    main()