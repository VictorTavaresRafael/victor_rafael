import boto3
import os
from datetime import datetime

def upload_to_s3(file_path, bucket_name):
    """
    Faz o upload de um arquivo para uma pasta particionada no S3,
    determinando a especificação a partir do nome do arquivo.
    """
    if not os.path.exists(file_path):
        print(f"❌ ERRO: O arquivo '{file_path}' não foi encontrado no container.")
        return

    file_name = os.path.basename(file_path)
    # Extrai o nome do arquivo sem a extensão para usar como 'especificação'
    spec = os.path.splitext(file_name)[0].capitalize() # Ex: 'series' -> 'Series'

    today = datetime.utcnow()
    s3_key = f"Raw/Local/CSV/{spec}/{today.strftime('%Y/%m/%d')}/{file_name}"

    s3_client = boto3.client('s3')

    print(f"\nIniciando o upload do arquivo '{file_name}'...")
    print(f"Bucket de destino: {bucket_name}")
    print(f"Caminho de destino: s3://{bucket_name}/{s3_key}")

    try:
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print(f"✅ Upload de '{file_name}' concluído com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro durante o upload de '{file_name}': {e}")

if __name__ == '__main__':
    # --- CONFIGURAÇÕES ---
    NOME_DO_BUCKET = 'desafio-sprint-5-victor-rafael'
    # Lista de arquivos a serem processados dentro do container
    # Os arquivos estarão em uma pasta 'data' dentro do container
    arquivos_para_upload = ['data/series.csv', 'data/movies.csv']
    # ---------------------

    if 'seu-bucket-aqui' in NOME_DO_BUCKET:
        print("❌ ERRO: O nome do bucket não foi alterado. Edite o script e insira o nome correto.")
    else:
        for arquivo in arquivos_para_upload:
            upload_to_s3(arquivo, NOME_DO_BUCKET)