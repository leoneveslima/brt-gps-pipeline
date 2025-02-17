-- CTE para selecionar os dados brutos da fonte 'dados_brt'
with source_data as (
    SELECT 
        codigo, -- Código do veículo
        latitude, -- Latitude da posição do veículo
        longitude, -- Longitude da posição do veículo
        velocidade -- Velocidade do veículo
    FROM {{ source('brt_source','dados_brt')}} -- Referencia a tabela que contém os dados
)

-- Retorna os dados processados para análise
SELECT 
    codigo,
    latitude,
    longitude,
    velocidade
FROM source_data