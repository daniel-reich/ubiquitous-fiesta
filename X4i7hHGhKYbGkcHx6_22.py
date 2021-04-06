
def average_index(letters):
  sum = 0
  for c in letters:
    sum += ord(c) - 96
  return round(sum/len(letters), 2)

