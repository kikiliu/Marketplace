select SHIPWRCK.Ship_Name
from
(select 
    SITES.Site_No
from
    (select 
        DIVEORDS.Destination
    from
        DIVECUST, DIVEORDS
    where
        DIVECUST.Name = 'Mary Rioux'
            and DIVEORDS.Customer_No = DIVECUST.Customer_No) as TEMP,
    DEST,
    SITES
where
    TEMP.Destination = DEST.Destination_Name
        and DEST.Destination_No = SITES.Destination_No) as TEMPSITE,
    SHIPWRCK
where
        TEMPSITE.Site_No = SHIPWRCK.Site_No


