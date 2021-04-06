
def unique_abbrev(abbs, words):
  al = []
  for x in abbs:
    temp = []
    for y in words:
      temp.append(y.startswith(x))
    al.append((temp))
  return sum(al[0]+al[1]+al[2]) == 3

