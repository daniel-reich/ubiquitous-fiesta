
import math
def encryption(txt):
  txt = txt.replace(" ","")
  rows = int(math.sqrt(len(txt)))
  if not float(rows) == float(math.sqrt(len(txt))):
    cols = rows + 1
  else:
    cols = rows
  if cols * rows < len(txt):
    rows += 1
  res = []
  for _ in range(rows):
    tmp = []
    for _ in range(cols):
      tmp.append(" ")
    res.append(tmp)
  
  i = 0 
  j = 0
  k = 0
  while i < len(txt):
    res[j][k] = txt[i]
    i += 1
    k += 1
    if k == len(res[0]):
      k = 0
      j += 1
  result = ""
  for j in range(len(res[0])):
    for i in range(len(res)):
      result += res[i][j]
    if not result[-1] == " ":
      result += " " 
  while result[-1] == " ":
    result = result[:-1]
    
  return result

