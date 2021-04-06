
def XO(txt):
  numX, numO = 0,0
  for i in range(len(txt)):
    if txt[i] == "x" or txt[i] == "X":
      numX = numX + 1
    if txt[i] == "o" or txt[i] == "O":
      numO = numO + 1
  return numX == numO

