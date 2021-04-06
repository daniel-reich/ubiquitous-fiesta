
from datetime import date
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
​
    sd = start_date.split(",")
    ed = end_date.split(",")
​
    sd = date(int(sd[0]),int(sd[1]),int(sd[2]))
    ed = date(int(ed[0]),int(ed[1]),int(ed[2]))
​
    delta = ed-sd
    d = delta.days
    if d < 0:
        return 'Invalid date'
    if end_read < start_read:
        return 'Invalid meter readings'
​
    charge = round((((d*stand)+((end_read-start_read)*tariff))*1.05),2)
​
    return '$' + str(charge)

