
from datetime import datetime
def how_unlucky(y):
    return sum(datetime(year=y, month=m, day=13).weekday() == 4
               for m in range(1, 13))

