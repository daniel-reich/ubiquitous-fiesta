
def manage_delays(train, dest, delay):
  for destination in train.destinations:
    if destination==dest:
      hour,min = train.expected_time.split(':')
      new_time = int(hour)*60 + int(min) + delay
      train.expected_time = '{:0>2}:{:0>2}'.format(new_time//60,new_time%60)

