
def time_sum(times):
  hrs, mins, secs = 0, 0, 0
  for time in times:
    hour, minute, sec = map(int, time.split(':'))
    hrs += hour
    mins += minute
    secs += sec
  mins += secs // 60
  secs = secs % 60
  hrs += mins // 60
  mins = mins % 60
  return [hrs, mins, secs]

