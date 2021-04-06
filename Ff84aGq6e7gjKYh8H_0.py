
def minutes_to_seconds(time):
  m, s = map(int, time.split(':'))
  return False if s >= 60 else m*60 + s

