with source as (

    select * from {{ ref('raw_screentime') }}

),

renamed as (
    select 
        character_name
        ,film_name
        ,episode
        ,proportion
        ,minutes
        ,release_year
        
    from source
)

select * from renamed