
  create view "postgres"."public"."brt_veiculos__dbt_tmp"
    
    
  as (
    with source_data as (
    SELECT 
        codigo,
        latitude,
        longitude,
        velocidade
    FROM "postgres"."public"."dados_brt" -- Referencia a tabela que contém os dados
)

SELECT 
    codigo,
    latitude,
    longitude,
    velocidade
FROM source_data
  );