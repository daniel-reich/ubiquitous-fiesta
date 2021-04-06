
def manage_delays(train, dest, delay):
  from datetime import datetime as dtime,timedelta
  delay = timedelta(minutes=int(delay))
  if dest in train.destinations:
    exp_time = dtime(1,1,1,hour=int(train.expected_time[:2]),minute=int(train.expected_time[3:]))
    new_time = exp_time + delay
    train.expected_time = str(new_time.hour)+':'
    if new_time.minute < 10:
      train.expected_time += '0'
    train.expected_time += str(new_time.minute)

