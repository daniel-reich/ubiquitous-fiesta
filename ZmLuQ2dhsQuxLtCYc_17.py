
from  datetime import  datetime ,timedelta
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
    s,e = datetime.strptime(start_date,"%Y,%m,%d").timestamp(), datetime.strptime(end_date,"%Y,%m,%d").timestamp()
    if s>e:return "Invalid date"
    elif end_read<start_read :return "Invalid meter readings"
    tt,tr = ((e-s)/86400)*stand,(end_read-start_read)*tariff
    return "$"+str(round((tr+tt)*1.05,2))

