
def encrypt(word):
  refn = {"a" : "0", "e": "1", "o" : "2", "u" : "3"}
  new = word[::-1]
  newl = list(new)
  for x in range(len(newl)):
    if newl[x] in refn:
      newl[x] = refn[newl[x]]
  new = ""
  for item in newl:
    new += item
  return new + "aca"

