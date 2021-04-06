
def average_index(letters):
  lst = [ord(i) - 96 for i in letters]
  return round(sum(lst) / len(lst), 2)

