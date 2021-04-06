
def high_low(txt):
  listofints = [int(i) for i in txt.split()]
  return str(max(listofints)) + " " + str(min(listofints))

