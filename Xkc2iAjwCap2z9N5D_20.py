
import datetime
def has_friday_13(month, year):
    x= datetime.datetime(year,month,13)
    return x.strftime("%A") == "Friday"

