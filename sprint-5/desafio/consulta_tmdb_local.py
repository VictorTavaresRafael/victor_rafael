import requests
import json
import time

# --- CONFIGURAÇÕES ---
# Chave de API v3 do TMDB
TMDB_API_KEY = "a300099b723d88520c7fb1fac5817994"

# Exemplo de ID do IMDB (tt0111161 - The Shawshank Redemption)
IMDB_ID_EXEMPLO = "tt0111161"
# ---------------------

def buscar_detalhes_tmdb(api_key, imdb_id):
    """
    Busca detalhes de um filme no TMDB usando seu ID do IMDB.
    Retorna o dicionário com os detalhes ou None se não encontrar.
    """
    print(f"Buscando dados para o IMDb ID: {imdb_id}")

    # --- ETAPA 1: Encontrar o ID do TMDB a partir do ID do IMDB ---
    try:
        find_url = f"https://api.themoviedb.org/3/find/{imdb_id}?api_key={api_key}&language=pt-BR&external_source=imdb_id"
        response_find = requests.get(find_url)
        response_find.raise_for_status()
        find_data = response_find.json()

        # O TMDB retorna resultados para filmes e séries, precisamos checar ambos
        results = find_data.get('movie_results', []) + find_data.get('tv_results', [])
        if not results:
            print(f"-> ❌ Nenhum resultado encontrado para {imdb_id}")
            return None

        tmdb_id = results[0]['id']
        # Determina se é filme ou série para a próxima chamada
        media_type = 'movie' if find_data.get('movie_results') else 'tv'
        print(f"-> ✅ ID do TMDB encontrado: {tmdb_id} (Tipo: {media_type})")

    except requests.exceptions.RequestException as e:
        print(f"-> ❌ Erro ao buscar pelo ID do IMDB: {e}")
        return None
        
    # --- ETAPA 2: Buscar os detalhes usando o ID do TMDB ---
    try:
        details_url = f"https://api.themoviedb.org/3/{media_type}/{tmdb_id}?api_key={api_key}&language=pt-BR"
        response_details = requests.get(details_url)
        response_details.raise_for_status()
        details_data = response_details.json()
        return details_data

    except requests.exceptions.RequestException as e:
        print(f"-> ❌ Erro ao buscar detalhes: {e}")
        return None


if __name__ == '__main__':
    detalhes = buscar_detalhes_tmdb(TMDB_API_KEY, IMDB_ID_EXEMPLO)
    if detalhes:
        print("\n\n--- Resposta final dos detalhes ---")
        # Imprime o JSON de forma legível
        print(json.dumps(detalhes, indent=2, ensure_ascii=False))