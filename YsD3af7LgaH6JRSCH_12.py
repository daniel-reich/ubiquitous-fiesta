
from datetime import datetime, timedelta
​
def time_adjust(now, hrs, mins, sec):
    dt = datetime.strptime(now, '%H:%M:%S')
    a = timedelta(hours=hrs, minutes=mins, seconds=sec)
    return (dt + a).strftime('%H:%M:%S')

