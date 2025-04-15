with source as (

    select * from {{ ref('raw_people') }}

),

renamed as (
    select 
        url as resource_url
        ,name as character_name
        ,height
        ,mass
        ,hair_color
        ,skin_color
        ,eye_color
        ,birth_year
        ,gender
        ,species
        
    from source
)

select * from renamed