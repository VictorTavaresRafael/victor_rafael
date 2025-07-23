import boto3
import os
from datetime import datetime

def upload_to_s3(file_path, bucket_name):
    """
    Faz o upload de um arquivo para uma pasta particionada por data no S3.
    """
    file_name = os.path.basename(file_path)
    today = datetime.utcnow()
    s3_key = f"Raw/Local/CSV/Series/{today.strftime('%Y/%m/%d')}/{file_name}"

    s3_client = boto3.client('s3')

    print(f"Iniciando o upload do arquivo '{file_name}' para o S3.")
    print(f"Bucket de destino: {bucket_name}")
    print(f"Caminho de destino: s3://{bucket_name}/{s3_key}")

    try:
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print("\n✅ Upload concluído com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro durante o upload: {e}")

if __name__ == '__main__':
    # --- CONFIGURAÇÕES ---
    # IMPORTANTE: Substitua pelo nome exato do seu bucket no S3
    NOME_DO_BUCKET = 'desafio-sprint-5-victor-rafael'
    CAMINHO_DO_ARQUIVO_LOCAL = 'series.csv'
    # ---------------------

    if 'seu-bucket-aqui' in NOME_DO_BUCKET:
        print("❌ ERRO: O nome do bucket não foi alterado. Edite o script e insira o nome correto.")
    elif not os.path.exists(CAMINHO_DO_ARQUIVO_LOCAL):
        print(f"❌ ERRO: O arquivo '{CAMINHO_DO_ARQUIVO_LOCAL}' não foi encontrado.")
    else:
        upload_to_s3(CAMINHO_DO_ARQUIVO_LOCAL, NOME_DO_BUCKET)