# <ins>BRT GPS Pipeline</ins>

Este projeto captura dados da API de GPS do BRT do Rio de Janeiro, armazena os dados em um banco de dados PostgreSQL e os transforma utilizando DBT.

## 📌 Tecnologias Utilizadas

- **Python** - Linguagem principal utilizada no projeto 
- **Prefect** - Para orquestração da pipeline de captura de dados
- **PostgreSQL** - Para armazenamento dos dados
- **DBT (Data Build Tool)** - Para transformação e modelagem dos dados
- **Docker** - Para facilitar a execução do ambiente

## 📂 Estrutura do Projeto
```sh
brt_gps/ 
│── data/                     # Armazena arquivos CSV gerados 
│── models/                   # Modelos do DBT 
├── brt_data_pipeline.py      # Pipeline Prefect para capturar os dados da API 
├── load_to_postgres.py       # Script para carregar os dados no PostgreSQL 
│── projeto_brt/              # Projeto DBT com modelos e configurações 
│── Dockerfile                # Arquivo para criar container do projeto 
│── requirements.txt          # Dependências do projeto 
```

## 🔧 Como Configurar e Rodar

1. **Clone o repositório**  
   ```sh
   git clone https://github.com/leoneveslima/brt-gps-pipeline.git
   cd brt-gps-pipeline
2. **Instale as dependências**
   ```sh
   pip install -r requirements.txt
3. **Configure o PostgreSQL**
   ```sh
   - Certifique-se de que tem um banco de dados PostgreSQL rodando.
   - Configure as credenciais no arquivo .env ou diretamente no script.
4. **Rode a pipeline Prefect**
   ```sh
   python scripts/brt_data_pipeline.py
5. **Execute o DBT para executar os dados**
   ```sh
   dbt run
6. **Resultado final**
   ```sh
   SELECT * FROM public.brt_veiculos LIMIT 10;
   ```
   ![image](https://github.com/user-attachments/assets/0a99081e-9902-42fc-8989-bd7799116ec4)
