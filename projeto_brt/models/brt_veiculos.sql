with source_data as (
    SELECT 
        codigo,
        latitude,
        longitude,
        velocidade
    FROM {{ source('fonte', 'postgres.dados_brt')}} -- Referencia a tabela que contém os dados
)

SELECT 
    codigo,
    latitude,
    longitude,
    velocidade
FROM source_data