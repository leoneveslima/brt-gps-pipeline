# scripts/brt_data_pipeline.py
import os
import time
import requests
import pandas as pd
from prefect import Flow, task
from datetime import datetime

# Definindo URL da API de onde os dados serão extraídos
data_url = "https://dados.mobilidade.rio/gps/brt"

# Caminho para armazenar os dados coletados
output_file = "data/brt_data.csv"

# Criação do diretório 'data' (onde serão armazenados os dados extraídos da API) caso não exista
if not os.path.exists('data'):
    os.makedirs('data')

# Tarefa Prefect: Faz a requisição na API e retornando os dados no formato JSON
@task
def fetch_data():
    response = requests.get(data_url)
    data = response.json()
    
    # Pegando apenas os veículos do JSON retornado
    if "veiculos" in data:
        return data["veiculos"]
    else:
        raise ValueError("A chave veículos não foi encontrada no JSON da API")

# Tarefa Prefect: Transforma os dados em DataFrame e salva em arquivo CSV
@task
def save_to_csv(data):
    df = pd.DataFrame(data)
    
    # Convertendo dataHora de milissegundos para datetime
    df['dataHora'] = pd.to_datetime(df['dataHora'], unit='ms')
    
    # Adicionando timestamp da execução
    df["timestamp"] = datetime.now()
    
    # Verifica se o arquivo já existe para decidir se deve incluir o cabeçalho
    if not os.path.isfile(output_file):
        df.to_csv(output_file, mode='w', index=False, header=True, encoding='utf-8')
    else:
        df.to_csv(output_file, mode='a', index=False, header=False, encoding='utf-8')

# Definição do fluxo de dados no Prefect
with Flow("BRT data Pipeline") as flow:
    data = fetch_data()
    save_to_csv(data)

# Loop para executar o fluxo a cada 60 segundos
if __name__ == "__main__":
    while True:
        flow.run()
        time.sleep(60)