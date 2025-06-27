# etl/etl.py

import pandas as pd
import os

INPUT_CSV_PATH = '/data/concert_tours_by_women.csv'
OUTPUT_CSV_PATH = '/volume/csv_limpo.csv'

def clean_data():
    """
    Lê o CSV de entrada, realiza a limpeza e salva o resultado.
    """
    print("Iniciando o processo de ETL...")

    output_dir = os.path.dirname(OUTPUT_CSV_PATH)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df = pd.read_csv(INPUT_CSV_PATH)
    
    df = df.rename(columns={'Adjustedgross (in 2022 dollars)': 'Adjusted gross (in 2022 dollars)'})

    years_split = df['Year(s)'].str.split(r'–|-', expand=True)

    df['Start year'] = pd.to_numeric(years_split[0])

    df['End year'] = pd.to_numeric(years_split[1]).fillna(df['Start year'])

    df['Start year'] = df['Start year'].astype(int)
    df['End year'] = df['End year'].astype(int)

    df = df.drop(columns=['Year(s)'])
    
    print(f"Colunas Finais Geradas: {df.columns.tolist()}")
    
    df.to_csv(OUTPUT_CSV_PATH, index=False)
    
    print(f"Dados limpos e salvos em {OUTPUT_CSV_PATH}")
    print("Processo de ETL concluído.")

if __name__ == "__main__":
    clean_data()