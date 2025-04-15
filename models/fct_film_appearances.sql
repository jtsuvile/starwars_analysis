with people_appearances as (select 
  film_url
  , 'person' as resource_type
  , trim(regexp_split_to_table(trim(characters, '[]'), ','), ''' ') as resource_url
  from {{ ref('stg_films') }}),

species_appearances as (select 
  film_url
  , 'species' as resource_type
  , trim(regexp_split_to_table(trim(species, '[]'), ','), ''' ') as resource_url
  from {{ ref('stg_films') }}),

all_film_appearances as (
    select * from people_appearances
    union all
    select * from species_appearances)

select * from all_film_appearances