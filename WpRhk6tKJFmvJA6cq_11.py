
from datetime import time, timedelta, datetime
​
def manage_delays(train, dest, delay):
  h, m = train.expected_time.split(':')
  expected = datetime(1, 1, 1, int(h), int(m))
  
  if dest in train.destinations:
    a = expected + timedelta(minutes=delay)
    train.expected_time = a.time().strftime('%H:%M')

