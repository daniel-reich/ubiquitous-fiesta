
def how_many_times(msg):
  counter = 0
  for char in msg:
    counter += ord(char)-96
  return counter

