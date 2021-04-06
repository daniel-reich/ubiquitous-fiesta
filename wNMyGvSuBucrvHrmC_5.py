
def number_of_repeats(string):
  length = len(string)
  for i in range(1, length):
    floor = length // i
    if floor * string[:i] == string:
      return floor
  return 1

