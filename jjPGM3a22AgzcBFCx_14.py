
def decrypt(lst):
  copyLst = lst
  fullRange = list(range(1, 27))
  for i in copyLst:
    fullRange.remove(i)
  return(chr(fullRange[0] + 64))

