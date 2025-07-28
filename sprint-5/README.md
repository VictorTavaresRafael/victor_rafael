# 📝 Sprint Readme: Jornada de Estudos em Big Data com Spark e AWS

Este documento resume as atividades e aprendizados adquiridos durante a sprint, focada no aprofundamento em tecnologias de Big Data, incluindo Apache Spark, PySpark e serviços de análise de dados da AWS.

---

## 📚 Cursos Realizados

Durante esta sprint, dediquei-me à realização de cursos que foram fundamentais para a expansão do meu conhecimento em ecossistemas de Big Data e cloud computing:

- **Formação Spark com PySpark: O Curso Completo**  
  Um estudo aprofundado sobre o Apache Spark, utilizando a linguagem Python (PySpark) para processamento de grandes volumes de dados.

- **AWS Skill Builder - Fundamentals of Analytics on AWS – Part 1**<br>
  [Certificado](./certificados/certificado-AWS-Fundamentals-of-Analytics.pdf)

- **AWS Skill Builder - Introduction to Amazon Athena**  
  [Certificado](./certificados/certificado-AWS-Introduction-to-Amazon-Athena.pdf)

- **AWS Skill Builder - Serverless Analytics**  
  [Certificado](./certificados/certificado-AWS-Serverless-Analytics.pdf)

---

## 📖 Leituras Complementares

Para solidificar a base teórica, realizei leituras técnicas sobre os pilares do processamento de Big Data:

- **Apache Hadoop:**  
  Estudo sobre sua arquitetura, componentes (como HDFS e MapReduce) e seu papel fundamental na fundação dos ecossistemas de Big Data.

- **Apache Spark:**  
  Leitura focada em entender sua arquitetura, o conceito de RDDs (Resilient Distributed Datasets), DataFrames, e suas vantagens em relação ao MapReduce do Hadoop, como o processamento em memória.

---

## 💻 Atividades Práticas

Para aplicar o conhecimento adquirido, desenvolvi duas atividades práticas principais, além do desafio da sprint.

---

### 1. Extração de Dados da API do TMDB (The Movie Database)

Nesta atividade, o objetivo foi criar um processo para extrair dados de filmes utilizando a API RESTful do TMDB.

**Passos Realizados:**

- **Criação de Conta e Obtenção de Chave de API:**  
  Criação de conta no portal do TMDB e solicitação de chave de API para uso pessoal.

- **Desenvolvimento do Script de Extração:**  
  Utilizando Python e as bibliotecas `requests` e `pandas`.

**Código-fonte desenvolvido:**

```python
import requests
import pandas as pd

# Sua chave de API está correta.
api_key = "a300099b723d88520c7fb1fac5817994"
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

print("Buscando dados na API do TMDB...")

response = requests.get(url)

# Verificar se a requisição foi bem-sucedida (código 200 significa OK)
if response.status_code == 200:
    # Todo o nosso processamento acontece DENTRO deste bloco 'if'
    
    # 1. Extrair os dados da resposta em formato JSON
    data = response.json()
    filmes_encontrados = data['results']
    print(f"Encontrados {len(filmes_encontrados)} filmes. Processando...")

    # 2. Loop para extrair as informações de cada filme
    lista_de_filmes = []
    for movie in filmes_encontrados:
        info_filme = {
            'Título': movie.get('title'),
            'Data de lançamento': movie.get('release_date'),
            'Visão geral': movie.get('overview'),
            'Votos': movie.get('vote_count'),
            'Média de votos': movie.get('vote_average')
        }
        lista_de_filmes.append(info_filme)
    
    # 3. Criar o DataFrame com os dados
    df_filmes = pd.DataFrame(lista_de_filmes)
    
    # 4. Configurar o Pandas para exibir a tabela completa
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    
    # 5. Exibir a tabela na tela
    print("\n--- Tabela de Filmes Extraídos ---")
    print(df_filmes)

    # 6. Salvar o arquivo CSV como evidência
    nome_arquivo_saida = 'filmes_extraidos_tmdb.csv'
    df_filmes.to_csv(nome_arquivo_saida, index=False, encoding='utf-8-sig')
    print(f"\n✅ Evidência gerada! Os dados foram salvos no arquivo: {nome_arquivo_saida}")

else:
    # Este bloco 'else' só é executado se a requisição falhar
    print(f"Erro ao acessar a API: Código {response.status_code}")
    print(f"Resposta: {response.text}")
```

---

### 2. Análise de Dados com Spark em um Ambiente Docker

Neste exercício prático, utilizei o framework Spark em um container Docker para processar e analisar um arquivo de texto.

**Passos Realizados:**

- **Setup do Ambiente Docker:**

```bash
docker pull jupyter/all-spark-notebook
```

- **Criação do Container:**

```bash
docker run -p 8888:8888 jupyter/all-spark-notebook
```

- **Execução no Spark Shell:**

```bash
docker exec -it <ID_DO_CONTAINER> pyspark
```

- **Contagem de Palavras com Spark:**

```python
# 1. Carregar o arquivo README.md como um RDD
textFile = spark.read.text("README.md").rdd.map(lambda r: r[0])

# 2. Quebrar cada linha em palavras, achatar a lista e contar cada palavra
wordCounts = textFile.flatMap(lambda line: line.split(" ")) \
                     .map(lambda word: (word, 1)) \
                     .reduceByKey(lambda a, b: a + b)

# 3. Coletar e exibir o resultado
for word, count in wordCounts.collect():
    print(f"{word}: {count}")
```

---

## 🚀 Desafio da Sprint

Além das atividades listadas, um desafio prático foi concluído para consolidar todos os aprendizados. Os detalhes, o código-fonte e as conclusões deste desafio estão documentados em seu próprio repositório:

[Desafio](./desafio)
