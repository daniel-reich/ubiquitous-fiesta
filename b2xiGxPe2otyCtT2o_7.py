
def how_many_times(msg):
  total_count = 0
  for char in msg:
    total_count += ord(char) - 96
  return total_count

