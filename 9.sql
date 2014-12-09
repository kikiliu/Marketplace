select 
    Destination_Name
from
    DEST
where
    DEST.Avg_Temp_F > 75
        and DEST.Travel_Cost < 4000