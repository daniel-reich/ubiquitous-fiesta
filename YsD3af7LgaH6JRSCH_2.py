
import datetime
​
def time_adjust(now, hrs, mins, sec):
    a = datetime.datetime.strptime(now, '%H:%M:%S')
    b = a + datetime.timedelta(hours=hrs,minutes=mins,seconds=sec)
​
    return str(b.hour).zfill(2) +':' + str(b.minute).zfill(2) + ":" + str(b.second).zfill(2)

