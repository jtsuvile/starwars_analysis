with source as (

    select * from {{ ref('raw_vehicles') }}

),

renamed as (
    select 
    
        url as resource_url
        ,name as vehicle_name
        ,model
        ,vehicle_class
        ,manufacturer
        ,cost_in_credits
        ,length
        ,max_atmosphering_speed
        ,crew
        ,passengers
        ,cargo_capacity
        ,consumables
        
    from source
)

select * from renamed