
def average_index(letters):
  al = ' abcdefghijklmnopqrstuvwxyz'
  return round(sum(al.index(x) for x in letters) / len(letters), 2)

