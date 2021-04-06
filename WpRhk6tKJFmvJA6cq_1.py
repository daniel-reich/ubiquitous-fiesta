
def manage_delays(train, dest, delay):
  if dest in train.destinations:
    h, m = (int(x) for x in train.expected_time.split(':'))
    m += delay
    if m > 59:
      h += m//60
      m %= 60
    train.expected_time = '{:02d}:{:02d}'.format(h,m)
  return train.expected_time

