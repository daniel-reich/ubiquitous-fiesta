
from datetime import datetime as dt, timedelta as delta
​
def manage_delays(train, dest, delay):
    if dest in train.destinations:
        train.expected_time = (dt.strptime(train.expected_time, '%H:%M') + delta(minutes=delay)).strftime('%H:%M')

