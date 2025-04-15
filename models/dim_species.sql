with source as (

    select * from {{ ref('stg_species') }}

),

renamed as (
    select 
    
        resource_url
        ,species_name
        ,classification
        ,designation
        ,average_height
        ,skin_colors
        ,hair_colors
        ,eye_colors
        ,average_lifespan
        ,language
        
    from source
)

select * from renamed