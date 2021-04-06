
from datetime import date
def days_until_2021(d):
    m,d,y = d.split("/")
    diff = (date(2021, 1, 1) - date(int(y), int(m), int(d))).days
    return "{} day{}".format(diff, ["s",""][diff==1])

