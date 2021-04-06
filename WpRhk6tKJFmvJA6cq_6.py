
from datetime import datetime, timedelta 
def manage_delays(train, dest, delay):
  if dest in train.destinations:
    x = datetime.strptime(train.expected_time, '%H:%M') + timedelta(minutes = delay)
    y = x.strftime('%H:%M')
    train.expected_time = y

