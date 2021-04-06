
from datetime import datetime, timedelta
def manage_delays(train, dest, delay):
  delay = timedelta(minutes=int(delay))
  arrival = datetime.strptime(train.expected_time, '%H:%M')
  if dest in train.destinations:
    train.expected_time = (arrival + delay).strftime('%H:%M')
  return train.expected_time

