select 
    DIVESTOK.Description, Rental_Price
from
    DIVEITEM,
    DIVEORDS,
	DIVESTOK
where
    DIVEORDS.VacationCost > 30000
		and DIVEITEM.Rental_Sale = 'Rental'
        and DIVEORDS.Order_No = DIVEITEM.Order_No
		and DIVEITEM.Item_No = DIVESTOK.Item_No
order by Rental_Price DESC