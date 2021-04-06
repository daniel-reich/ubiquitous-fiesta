
from datetime import timedelta
​
def manage_delays(train, dest, delay):
    if dest in train.destinations:
        L = [int(i) for i in train.expected_time.split(':')]
        t_init = timedelta(hours=L[0], minutes=L[1])
        t_add = timedelta(minutes=delay)
        t = t_init + t_add
        train.expected_time = str(t)[:5]

