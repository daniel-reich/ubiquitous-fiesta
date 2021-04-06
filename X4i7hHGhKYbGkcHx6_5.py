
def average_index(letters):
  return round(sum(ord(x)-ord('a')+1 for x in letters)/len(letters),2)

