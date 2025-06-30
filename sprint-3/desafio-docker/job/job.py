# job/job.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

CLEAN_CSV_PATH = '/volume/csv_limpo.csv'
ANSWERS_TXT_PATH = '/volume/respostas.txt'
CHART_Q4_PATH = '/volume/Q4.png'
CHART_Q5_PATH = '/volume/Q5.png'

def analyze_data():
    """
    Lê os dados limpos, responde às perguntas e gera os artefatos de saída.
    """
    print("Iniciando o processo de análise (Job)...")

    df = pd.read_csv(CLEAN_CSV_PATH)
    gross_cols = ['Actual gross', 'Adjusted gross (in 2022 dollars)', 'Average gross', 'Shows']
    for col in gross_cols:

        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.replace(r'[^\d.]', '', regex=True)
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.dropna(subset=gross_cols) 

    artist_counts = df['Artist'].value_counts()
    artist_avg_gross = df.groupby('Artist')['Actual gross'].mean()
    artist_stats = pd.concat([artist_counts, artist_avg_gross], axis=1)
    artist_stats.columns = ['appearances', 'average_gross']
    max_appearances = artist_stats['appearances'].max()
    top_artists = artist_stats[artist_stats['appearances'] == max_appearances]
    q1_artist = top_artists['average_gross'].idxmax()
    q1_answer = f"A artista que mais aparece e tem a maior média de faturamento é: {q1_artist}"

    one_year_tours = df[df['Start year'] == df['End year']]
    q2_tour = one_year_tours.loc[one_year_tours['Average gross'].idxmax()]
    q2_answer = f"A turnê em um único ano com maior média de faturamento é: {q2_tour['Tour title']} por {q2_tour['Artist']}"

    df['gross_per_show'] = df['Adjusted gross (in 2022 dollars)'] / df['Shows']
    top_3_tours = df.nlargest(3, 'gross_per_show')
    q3_answer_lines = ["As 3 turnês com o show mais lucrativo são:"]
    for i, row in top_3_tours.iterrows():
        q3_answer_lines.append(f"- {row['Tour title']} ({row['Artist']}): ${row['gross_per_show']:,.2f} por show.")
    q3_answer = "\n".join(q3_answer_lines)
    
    with open(ANSWERS_TXT_PATH, 'w', encoding='utf-8') as f:
        f.write("Q1:\n")
        f.write(f"--- {q1_answer}\n\n")
        f.write("Q2:\n")
        f.write(f"--- {q2_answer}\n\n")
        f.write("Q3:\n")
        f.write(f"--- {q3_answer}\n")
    print(f"Respostas salvas em {ANSWERS_TXT_PATH}")

    artist_total_gross = df.groupby('Artist')['Actual gross'].sum()
    artist_stats_q4 = pd.concat([artist_counts, artist_total_gross], axis=1)
    artist_stats_q4.columns = ['appearances', 'total_gross']
    max_appearances_q4 = artist_stats_q4['appearances'].max()
    top_artists_q4 = artist_stats_q4[artist_stats_q4['appearances'] == max_appearances_q4]
    q4_artist_name = top_artists_q4['total_gross'].idxmax()
    
    artist_df = df[df['Artist'] == q4_artist_name]
    yearly_gross = artist_df.groupby('Start year')['Actual gross'].sum().reset_index()

    plt.figure(figsize=(12, 7))
    sns.lineplot(x='Start year', y='Actual gross', data=yearly_gross, marker='o')
    plt.title(f'Faturamento Anual das Turnês de {q4_artist_name}')
    plt.xlabel('Ano de Início da Turnê')
    plt.ylabel('Faturamento Bruto (em centenas de milhões)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(CHART_Q4_PATH)
    print(f"Gráfico da Q4 salvo em {CHART_Q4_PATH}")
    plt.close()

    artist_show_counts = df.groupby('Artist')['Shows'].sum().nlargest(5).reset_index()
    
    plt.figure(figsize=(12, 7))
    sns.barplot(x='Shows', y='Artist', data=artist_show_counts, palette='viridis', orient='h')
    plt.title('Top 5 Artistas por Número Total de Shows')
    plt.xlabel('Número Total de Shows')
    plt.ylabel('Artista')
    plt.tight_layout()
    plt.savefig(CHART_Q5_PATH)
    print(f"Gráfico da Q5 salvo em {CHART_Q5_PATH}")
    plt.close()

    print("Processo de análise concluído.")

if __name__ == "__main__":
    analyze_data()