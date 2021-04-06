
def average_index(letters):
  sum_ords = 0
  for i in letters:
    sum_ords += ord(i) - 96
  return round(sum_ords / len(letters), 2)

