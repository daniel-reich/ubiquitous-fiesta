
def manage_delays(train, dest, delay):
  hr_min = train.expected_time.split(':')
  for d in train.destinations:
    if d == dest:
      hr_min[1] = int(hr_min[1]) + delay
  if int(hr_min[1]) > 59:
    hr_min[0] = int(hr_min[0]) + int(hr_min[1]/60)
    hr_min[1] = hr_min[1] % 60
  if len(str(hr_min[1])) < 1.5:
    train.expected_time = str(hr_min[0]) + ':0' + str(hr_min[1])
  else:
    train.expected_time = str(hr_min[0]) + ':' + str(hr_min[1])

