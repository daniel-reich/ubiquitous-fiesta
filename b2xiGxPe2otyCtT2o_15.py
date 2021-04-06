
def how_many_times(msg):
  times = 0
  for i in range(len(msg)):
    times = times + (ord(msg[i])-96)
  return times

