select 
    count(BIOSITE.Site_No)
from
    BIOLIFE,
    BIOSITE
where
    BIOLIFE.Common_Name = 'Nassau Grouper'
        and BIOLIFE.Species_No = BIOSITE.Species_No

