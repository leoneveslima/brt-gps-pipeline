import pandas as pd
from sqlalchemy import create_engine

# Caminho do arquivo CSV gerado pela pipeline 
csv_file_path = 'C:/Users/lrnli/brt_gps/data/brt_data.csv'

# Carrega os dados do CSV para um DataFrame
df = pd.read_csv(csv_file_path)

# Criando a conexão com o banco de dados PostgreSQL
db_url = 'postgresql://postgres:admin@localhost:5432/postgres'
engine = create_engine(db_url)

# Carregar o DataFrame no PostgreSQL (em uma tabela chamada "dados_brt")
df.to_sql('dados_brt', engine, if_exists='replace', index=False)