
def average_index(letters):
  alphabet = ' abcdefghijklmnopqrstuvwxyz'
  return round(sum([alphabet.index(x.lower()) for x in letters]) / len(letters),2)

