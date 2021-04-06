
def manage_delays(train, dest, delay):
  if dest in train.destinations:
    h, m = map(int, train.expected_time.split(':'))
    m += delay
    h += m//60
    train.expected_time = '{:02d}:{:02d}'.format(h%24, m%60)

