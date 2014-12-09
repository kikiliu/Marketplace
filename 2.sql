select 
    BIOLIFE.Species_Name
from
    (select 
        DIVEORDS.Destination
    from
        DIVECUST, DIVEORDS
    where
        DIVECUST.Name = 'Mary Rioux'
            and DIVEORDS.Customer_No = DIVECUST.Customer_No) as TEMP,
    DEST,
    SITES,
    BIOSITE,
	BIOLIFE
where
    TEMP.Destination = DEST.Destination_Name
        and DEST.Destination_No = SITES.Destination_No
        and SITES.Site_No = BIOSITE.Site_No
		and BIOSITE.Species_No = BIOLIFE.Species_No
group by BIOLIFE.Species_Name
