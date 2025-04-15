with source as (

    select * from {{ ref('raw_species') }}

),

renamed as (
    select 
    
        url as resource_url
        ,name as species_name
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