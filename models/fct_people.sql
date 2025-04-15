with renamed as (
    select 
    p.resource_url
    ,p.character_name
    ,height
    ,mass
    ,hair_color
    ,skin_color
    ,eye_color
    ,birth_year
    ,gender
    ,coalesce(
        NULLIF(p.species,''),
        e.species_url) as species
    from {{ ref('stg_people') }} p
    left join {{ ref('stg_errata_people') }} e
    on p.resource_url = e.resource_url 
)

select * from renamed