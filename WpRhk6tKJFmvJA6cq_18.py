
from datetime import datetime,timedelta
def manage_delays(train, dest, delay):
  if dest in train.destinations:
    eta = datetime.strptime(train.expected_time,'%H:%M')
    eta+=timedelta(minutes=delay)
    train.expected_time = eta.strftime("%H:%M")

