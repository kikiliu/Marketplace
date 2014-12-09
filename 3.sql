select 
    SHIPWRCK.Ship_Name
from
    DEST,
    SHIPWRCK,
    SITES
where
    DEST.Destination_Name = 'New Jersey'
        and SHIPWRCK.Interest = 'Treasure'
        and DEST.Destination_No = SITES.Destination_No
        and SITES.Site_No = SHIPWRCK.Site_No