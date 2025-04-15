with source as (

    select * from {{ ref('errata_people') }}

),

renamed as (
    select 

        url as resource_url
        ,name as character_name
        ,species as species_url
        
    from source
)

select * from renamed