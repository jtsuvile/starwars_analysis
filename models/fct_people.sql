with source as (

    select * from {{ ref('stg_people') }}

),

renamed as (
    select 

        resource_url
        ,character_name
        ,height
        ,mass
        ,hair_color
        ,skin_color
        ,eye_color
        ,birth_year
        ,gender
        ,trim(trim(species, '[]'), ''' ') as species
        
    from source
)

select * from renamed