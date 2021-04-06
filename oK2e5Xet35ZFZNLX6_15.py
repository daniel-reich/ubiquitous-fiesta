
def neighboring(txt):
  for i in range(1,len(txt)):
    if abs(ord(txt[i])-ord(txt[i-1]))!=1:
      return False
  return True

