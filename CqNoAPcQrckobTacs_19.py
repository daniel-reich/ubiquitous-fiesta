
def missing_letter(lst):
  newLst = []
  for l in lst:
    newLst.append(ord(l))
    
  for i in range(0,len(newLst)-1):
    if newLst[i] != (newLst[i+1] - 1):
      return chr(newLst[i]+1)

