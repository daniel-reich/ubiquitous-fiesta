
def isMagic(square):
  if not square:
    return True
  square1 = list(map(list,zip(*square)))
  chk = sum(square[0])
  if any(sum(square[i])!= chk or sum(square1[i])!=chk for i in range(len(square))):
    return False
  tot1,tot2,tot3 = 0,0,0
  for i in range(len(square)):
    tot1 += square[i][i]
    tot2 += square1[i][i]
    tot3 += sum(square[i])
  if tot3 != sum(range(1,len(square)**2+1)):
    return False
  if tot1 !=  chk or tot2 != chk:
    return False
  return True

