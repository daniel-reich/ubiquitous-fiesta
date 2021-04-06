
def high_low(txt):
  newlst = list(map(lambda x: int(x), txt.split(' ')))
  str1 = str(max(newlst))
  str2 = str(min(newlst))
  finalstr = str1 + " " + str2
  return finalstr

