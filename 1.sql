select 
    DIVECUST.Name,
    DIVECUST.Street,
    DIVECUST.City,
    DIVECUST.State_Prov,
    DIVECUST.Country,
    DIVECUST.Zip_Postal_Code
from
    DIVEITEM,
    DIVECUST,
    DIVESTOK,
    DIVEORDS
where
    DIVESTOK.Equipment_Class = 'Mask'
        and DIVESTOK.Item_No = DIVEITEM.Item_No
        and DIVEITEM.Rental_Sale = 'Rental'
        and DIVEITEM.Order_No = DIVEORDS.Order_No
        and DIVEORDS.Customer_No = DIVECUST.Customer_No

