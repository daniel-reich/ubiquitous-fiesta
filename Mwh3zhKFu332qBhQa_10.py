
def guess_sequence(n):
  num = 90
  interval = 150
  i = 1
  while i < n:
    num += interval
    interval += 60
    i += 1
  return num

