with people_appearances as (select 
  url as film_url
  , 'person' as resource_type
  , trim(regexp_split_to_table(trim(characters, '[]'), ','), ''' ') as resource_url
  from {{ ref('raw_films') }}),

species_appearances as (select 
  url as film_url
  , 'species' as resource_type
  , trim(regexp_split_to_table(trim(species, '[]'), ','), ''' ') as resource_url
  from {{ ref('raw_films') }}
  ),

starship_appearances as (select 
  url as film_url
  , 'starship' as resource_type
  , trim(regexp_split_to_table(trim(starships, '[]'), ','), ''' ') as resource_url
  from {{ ref('raw_films') }}
  ),
  
vehicle_appearances as (select
    url as film_url
  , 'vehicle' as resource_type
  , trim(regexp_split_to_table(trim(vehicles, '[]'), ','), ''' ') as resource_url
  from {{ ref('raw_films') }}
  ),

all_film_appearances as (
    select * from people_appearances
    union all
    select * from species_appearances
    union all
    select * from starship_appearances
    union all
    select * from vehicle_appearances
    )

select * from all_film_appearances