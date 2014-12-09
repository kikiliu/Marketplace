select 
    Category, count(*)
from
    BIOLIFE
group by Category
order by count(*) DESC