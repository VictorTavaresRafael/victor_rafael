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