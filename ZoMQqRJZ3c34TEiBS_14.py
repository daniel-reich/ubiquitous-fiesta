
import re
​
def playfair(txt, keyword):
  grid = []
  temp = []
  letters = list("abcdefghijklmnopqrstuvwxyz")
  for i in keyword:
    if i in letters:
      if i == "i" or i == "j":
        letters.remove("i")
        letters.remove("j")
        temp.append("ij")
      else:
        letters.remove(i)
        temp.append(i)
      if len(temp) == 5:
        grid.append(temp)
        temp = []
  for i in letters:
    if i == "j":
      temp.append("ij")
    elif i != "i":
      temp.append(i)
    if len(temp) == 5:
      grid.append(temp)
      temp = []
  decrypt = not re.search("\W",txt) and txt == txt.upper()
  txt = re.sub("\W","",txt).lower()
  i = 0
  while i <= len(txt)-2:
    if txt[i] == txt[i+1] or ((txt[i] == "i" or txt[i] == "j") and (txt[i+1] == "i" or txt[i+1] == "j")):
      txt = txt[:i+1]+"x"+txt[i+1:]
    i += 2
  if len(txt)%2 == 1:
    txt += "x"
  txt = [txt[i:i+2] for i in range(0,len(txt),2)]
  ctxt = ""
  for pair in txt:
    l1, l2 = pair[0], pair[1]
    if l1 == "i" or l1 == "j":
      l1 = "ij"
    if l2 == "i" or l2 == "j":
      l2 = "ij"
    for row in range(len(grid)):
      if l1 in grid[row]:
        row1 = row
        col1 = grid[row].index(l1)
      if l2 in grid[row]:
        row2 = row
        col2 = grid[row].index(l2)
    if row1 == row2:
      if decrypt:
        col1 = (col1-1)%5
        col2 = (col2-1)%5
      else:
        col1 = (col1+1)%5
        col2 = (col2+1)%5
    elif col1 == col2:
      if decrypt:
        row1 = (row1-1)%5
        row2 = (row2-1)%5
      else:
        row1 = (row1+1)%5
        row2 = (row2+1)%5
    else:
      col1, col2 = col2, col1
    l1, l2 = grid[row1][col1], grid[row2][col2]
    if l1 == "ij":
      l1 = "i"
    if l2 == "ij":
      l2 = "i"
    ctxt += l1+l2
  return ctxt.upper()

