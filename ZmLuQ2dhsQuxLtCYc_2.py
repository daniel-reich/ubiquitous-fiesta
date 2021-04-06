
from datetime import datetime as dt
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
    t1 = dt.strptime(start_date, "%Y,%m,%d")
    t2 = dt.strptime(end_date, "%Y,%m,%d")
    if t2 < t1:
        return "Invalid date"
    if end_read < start_read:
        return "Invalid meter readings"
    res = ((end_read - start_read) * tariff + (t2 - t1).days * stand) * 1.05
    return "${:.2f}".format(res)

