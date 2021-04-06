
def microwave_buttons(time):
  c = 0
  min, sec = map(int, time.split(':'))
  secs = min * 60 + sec
  if secs % 30 == 0 and 0 < secs // 30 < 3:
    c += secs // 30
  elif min != 0:
    c += 4 if min > 9 else 3
  elif sec != 0:
    c += 2
  return c + 1

