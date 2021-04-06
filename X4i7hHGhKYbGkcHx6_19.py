
def average_index(letters):
  return round(sum(ord(i) - 96 for i in letters)/len(letters),2)

