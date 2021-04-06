
def neighboring(txt):
  for i in range(len(txt)-1):
    if abs(ord(txt[i])-ord(txt[i+1]))!=1: return False
  return True

