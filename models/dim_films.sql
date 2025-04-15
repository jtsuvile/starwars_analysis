with source as (

    select * from {{ ref('stg_films') }}

),

renamed as (
    select 
    
        film_url
        ,title
        ,episode_id
        ,opening_crawl
        ,director
        ,producer
        ,release_date

    from source
)

select * from renamed