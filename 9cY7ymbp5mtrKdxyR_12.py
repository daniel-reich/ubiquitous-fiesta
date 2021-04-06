
def encryption(txt):
  import math
  final = ""
  lst = []
  nospace = txt.replace(" ","")
  rows = math.floor((len(nospace) ** 0.5))
  cols = math.ceil((len(nospace) ** 0.5))
  if rows * cols < len(nospace):
    rows += 1
  for i in range(rows):
    sublist = []
    for j in range(cols):
      try:
        sublist.append(nospace[cols*i + j])
      except:
        continue
    lst.append(sublist)
  #print(lst)
  for k in range(len(lst[0])):
    for l in range(len(lst)):
      try:
        final += lst[l][k]
      except:
        continue
    if k == (len(lst[0]) -1):
      break
    final += " "
  return final

