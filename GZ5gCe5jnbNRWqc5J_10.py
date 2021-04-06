
from datetime import datetime as dt
def first_tuesday_of_the_month(y, m):
    return ("{}-{:0>2}-{:0>2}".format(y, m, 1 + (1 - dt(year=y, month=m, day=1)
                                                 .weekday()) % 7))

