
def average_index(letters):
  big = 0
  for x in letters:
    big += ord(x) - 96
  return round(big/len(letters), 2)

