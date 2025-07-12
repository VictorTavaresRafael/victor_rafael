# analisar_migracao.py (Versão Final com Salvamento Local)

import os
import pandas as pd
# import boto3 <- Não precisamos mais de boto3 para esta versão
# from dotenv import load_dotenv <- E nem de dotenv
from io import StringIO
import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def carregar_dados(caminho_arquivo):
    """Carrega os dados de migração a partir de um arquivo CSV."""
    try:
        logging.info(f"Carregando dados de: {caminho_arquivo}")
        df = pd.read_csv(caminho_arquivo, sep=';', encoding='latin-1')
        df['TOTAL'] = pd.to_numeric(df['TOTAL'], errors='coerce')
        df.dropna(subset=['TOTAL'], inplace=True)
        df['TOTAL'] = df['TOTAL'].astype(int)
        logging.info("Dados carregados e limpos com sucesso.")
        return df
    except FileNotFoundError:
        logging.error(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
        return None
    except Exception as e:
        logging.error(f"Ocorreu um erro ao carregar os dados: {e}")
        return None

def analisar_por_nacionalidade(df):
    """Analisa o total de pessoas por nacionalidade."""
    logging.info("Analisando por nacionalidade...")
    analise = df.groupby('NACIONALIDADE')['TOTAL'].sum().reset_index()
    analise = analise.sort_values(by='TOTAL', ascending=False)
    logging.info("Análise por nacionalidade concluída.")
    return analise.head(20)

def analisar_por_uf(df):
    """Analisa o total de movimentos por UF de atendimento."""
    logging.info("Analisando por UF de atendimento...")
    analise = df.groupby('UF_ATENDIMENTO')['TOTAL'].sum().reset_index()
    analise = analise.sort_values(by='TOTAL', ascending=False)
    logging.info("Análise por UF de atendimento concluída.")
    return analise

def analisar_por_classificacao(df):
    """Analisa o total de movimentos por tipo de classificação."""
    logging.info("Analisando por classificação do movimento...")
    analise = df.groupby('CLASSIFICACAO')['TOTAL'].sum().reset_index()
    analise = analise.sort_values(by='TOTAL', ascending=False)
    logging.info("Análise por classificação concluída.")
    return analise

def salvar_localmente(df, nome_arquivo):
    """Salva o DataFrame como um arquivo CSV localmente."""
    if df is None or df.empty:
        logging.warning(f"DataFrame para '{nome_arquivo}' está vazio. Salvamento cancelado.")
        return
    try:
        # Cria uma pasta 'resultados' se ela não existir
        if not os.path.exists('resultados'):
            os.makedirs('resultados')
        
        caminho_completo = os.path.join('resultados', nome_arquivo)
        df.to_csv(caminho_completo, index=False)
        logging.info(f"Arquivo '{caminho_completo}' salvo com sucesso localmente.")
    except Exception as e:
        logging.error(f"Falha ao salvar o arquivo localmente: {e}")

def main():
    """Função principal que orquestra a execução do script."""
    caminho_dados = "dados/STI_MOVIMENTO_2025_06.csv"
    df_migracao = carregar_dados(caminho_dados)

    if df_migracao is not None:
        # 1. Análise por Nacionalidade
        df_nacionalidade = analisar_por_nacionalidade(df_migracao)
        print("\n--- Top 20 Nacionalidades por Total de Pessoas ---")
        print(df_nacionalidade)
        salvar_localmente(df_nacionalidade, "analise_nacionalidade.csv")
        
        # 2. Análise por UF
        df_uf = analisar_por_uf(df_migracao)
        print("\n--- Total de Movimentos por UF de Atendimento ---")
        print(df_uf)
        salvar_localmente(df_uf, "analise_uf.csv")

        # 3. Análise por Classificação
        df_classificacao = analisar_por_classificacao(df_migracao)
        print("\n--- Total de Movimentos por Classificação ---")
        print(df_classificacao)
        salvar_localmente(df_classificacao, "analise_classificacao.csv")

if __name__ == "__main__":
    main()