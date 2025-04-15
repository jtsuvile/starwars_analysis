with source as (

    select * from {{ ref('raw_films') }}

),

renamed as (
    select 
        url as film_url
        ,title
        ,episode_id
        ,opening_crawl
        ,director
        ,producer
        ,release_date
        ,species
        ,characters

    from source
)

select * from renamed