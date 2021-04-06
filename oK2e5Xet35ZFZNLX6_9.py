
def neighboring(txt):
  return all(abs(ord(txt[i])-ord(txt[i+1]))==1 for i in range(len(txt)-1))

