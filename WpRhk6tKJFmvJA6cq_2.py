
from datetime import timedelta
def manage_delays(train, dest, delay):
    if dest in train.destinations:
        H, M = t.expected_time.split(":")
        h2 = delay // 60
        m2 =delay % 60
        delay_obj = timedelta(hours=h2, minutes=m2)
​
        expected_time_obj = timedelta(hours=int(H), minutes=int(M))
        t.expected_time = str(expected_time_obj + delay_obj)[:5]

