
def how_many_times(msg):
  b = []
  for x in msg:
    b.append(ord(x) - 96)
  return sum(b)

