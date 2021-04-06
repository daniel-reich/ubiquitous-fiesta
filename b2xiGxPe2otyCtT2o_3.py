
def how_many_times(msg):
  return sum([ord(x.lower())-96 for x in msg])

