import pandas as pd
import json
import time
import requests
import boto3
import os

# A função buscar_detalhes_tmdb continua a mesma...
def buscar_detalhes_tmdb(api_key, imdb_id):
    """Busca detalhes de uma obra no TMDB a partir do seu ID do IMDB."""
    print(f"Buscando dados para o IMDb ID: {imdb_id}")
    try:
        find_url = f"https://api.themoviedb.org/3/find/{imdb_id}?api_key={api_key}&language=pt-BR&external_source=imdb_id"
        response_find = requests.get(find_url)
        response_find.raise_for_status()
        find_data = response_find.json()
        results = find_data.get('movie_results', []) + find_data.get('tv_results', [])
        if not results:
            print(f"-> ❌ Nenhum resultado encontrado para {imdb_id}")
            return None
        tmdb_id = results[0]['id']
        media_type = 'movie' if find_data.get('movie_results') else 'tv'
        details_url = f"https://api.themoviedb.org/3/{media_type}/{tmdb_id}?api_key={api_key}&language=pt-BR"
        response_details = requests.get(details_url)
        response_details.raise_for_status()
        details_data = response_details.json()
        print(f"-> ✅ Detalhes encontrados para {imdb_id}")
        return details_data
    except requests.exceptions.RequestException as e:
        print(f"-> ❌ Erro na chamada da API para {imdb_id}: {e}")
        return None

def find_latest_s3_object(bucket, prefix, s3_client):
    """Encontra o objeto modificado mais recentemente em um bucket do S3."""
    print(f"Procurando pelo objeto mais recente no prefixo: {prefix}")
    try:
        response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
        if 'Contents' not in response:
            print(f"-> ⚠️ Nenhum objeto encontrado no prefixo.")
            return None
        latest_object = sorted(response['Contents'], key=lambda obj: obj['LastModified'], reverse=True)[0]
        print(f"-> ✅ Objeto mais recente encontrado: {latest_object['Key']}")
        return latest_object['Key']
    except Exception as e:
        print(f"-> ❌ Erro ao listar objetos: {e}")
        return None

def lambda_handler(event, context):
    TMDB_API_KEY = os.environ.get('TMDB_API_KEY')
    BUCKET_NAME = os.environ.get('BUCKET_NAME')
    
    s3_client = boto3.client('s3')
    dados_coletados = []
    prefixos = ['Raw/Local/CSV/Movies/', 'Raw/Local/CSV/Series/']
    
    for prefix in prefixos:
        key_s3_csv = find_latest_s3_object(BUCKET_NAME, prefix, s3_client)
        if key_s3_csv:
            try:
                print(f"Processando o arquivo '{key_s3_csv}' em pedaços (chunks)...")
                response = s3_client.get_object(Bucket=BUCKET_NAME, Key=key_s3_csv)
                
                # Leitura em chunks para otimizar o uso de memória
                chunk_iterator = pd.read_csv(response['Body'], delimiter='|', chunksize=100000, low_memory=False)
                
                all_unique_ids = set()
                for chunk in chunk_iterator:
                    all_unique_ids.update(chunk['id'].unique())
                
                print(f"Total de IDs únicos encontrados no arquivo: {len(all_unique_ids)}")
                # Pega uma amostra de 5 IDs únicos para processar
                ids_para_buscar = list(all_unique_ids)[:5]

                for imdb_id in ids_para_buscar:
                    detalhes = buscar_detalhes_tmdb(TMDB_API_KEY, imdb_id)
                    if detalhes:
                        detalhes['imdb_id'] = imdb_id
                        dados_coletados.append(detalhes)
                    time.sleep(0.5)
            except Exception as e:
                print(f"❌ ERRO ao processar o arquivo {key_s3_csv}: {e}")
                continue

    if dados_coletados:
        from datetime import datetime
        hoje = datetime.utcnow()
        nome_arquivo_json = f"tmdb_details_{hoje.strftime('%Y%m%d_%H%M%S')}.json"
        key_s3_json = f"Raw/TMDB/JSON/Details/{hoje.strftime('%Y/%m/%d')}/{nome_arquivo_json}"
        
        print(f"\nColeta finalizada. {len(dados_coletados)} registros obtidos.")
        print(f"Salvando JSON em: s3://{BUCKET_NAME}/{key_s3_json}")

        s3_client.put_object(
            Bucket=BUCKET_NAME, Key=key_s3_json,
            Body=json.dumps(dados_coletados, indent=2, ensure_ascii=False),
            ContentType='application/json'
        )
        print("✅ Sucesso! O arquivo JSON foi salvo no S3.")
        return {'statusCode': 200, 'body': json.dumps(f'Sucesso! {len(dados_coletados)} registros salvos em {key_s3_json}')}
    else:
        return {'statusCode': 200, 'body': json.dumps('Nenhum dado novo foi coletado.')}