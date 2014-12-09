select DIVECUST.Name, DIVECUST.Phone
from DIVEORDS, DIVECUST
where DIVEORDS.CcExpDate < now()
and DIVECUST.Customer_No = DIVEORDS.Customer_No