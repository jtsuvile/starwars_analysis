with source as (

    select * from {{ ref('raw_starships') }}

),

renamed as (
    select 
    
        url as resource_url
        ,name as starship_name
        ,model
        ,starship_class
        ,manufacturer
        ,cost_in_credits
        ,length
        ,max_atmosphering_speed
        ,hyperdrive_rating
        ,MGLT
        ,crew
        ,passengers
        ,cargo_capacity
        ,consumables

    from source
)

select * from renamed