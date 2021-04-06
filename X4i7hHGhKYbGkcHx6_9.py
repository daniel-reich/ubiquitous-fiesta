
def average_index(letters):
  return round(sum(ord(x)-96 for x in letters)/len(letters),2)

