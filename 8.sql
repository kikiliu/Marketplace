select 
    DIVECUST.Name
from
    DIVESTOK,
    DIVEITEM,
    DIVEORDS,
    DIVECUST
where
    DIVESTOK.Description like '%teal%'
        and DIVESTOK.Item_No = DIVEITEM.Item_No
        and DIVEITEM.Order_No = DIVEORDS.Order_No
        and DIVEORDS.Customer_No = DIVECUST.Customer_No
group by DIVECUST.Customer_No
