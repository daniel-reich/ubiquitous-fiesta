
from datetime import date
def get_day(day):
    secs = day.split('/')
    d = date(int(secs[2]), int(secs[0]), int(secs[1]))
    return d.strftime("%A")

