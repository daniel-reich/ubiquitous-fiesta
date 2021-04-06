
def how_many_times(msg):
  return sum([int(ord(i)) for i in msg])- 96*len(msg)

