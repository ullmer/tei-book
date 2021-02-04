select count(*) from enFacetCountries;
select distinct region from enFacetWorldRegions;
select count (distinct region) from enFacetWorldRegions;
select distinct subregion from enFacetWorldRegions where region="Americas";

