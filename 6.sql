select 
    DIVECUST.name
from
    DIVECUST,
    DIVEORDS
where
    DIVEORDS.PaymentMethod = 'Cash'
        and DIVEORDS.Customer_No = DIVECUST.Customer_No