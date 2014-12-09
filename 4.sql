select DIVECUST.Name
from DIVECUST, DIVEORDS, DIVEITEM, DIVESTOK
where DIVEITEM.Rental_Sale = 'Rental'
and DIVEITEM.Order_No = DIVEORDS.Order_No
and DIVECUST.Customer_No = DIVEORDS.Customer_No
and DIVEITEM.Item_No = DIVESTOK.Item_No
order by Qty * Rental_Price DESC
limit 1