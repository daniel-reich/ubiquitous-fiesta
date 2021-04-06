
def inator_inator(inv):
  l = len(inv)
  if inv[-1] in ["a" , "e", "i", "o", "u", "A" , "E", "I", "O", "U"]:
    inv = inv + "-inator"
  else:
    inv = inv + "inator"
  return inv + " " + str(l*1000)

