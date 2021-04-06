
def neighboring(txt):
  return all(abs(ord(txt[i]) - ord(txt[i-1]))==1 and abs(ord(txt[i]) - ord(txt[i+1]))==1 for i in range(1,len(txt)-1))

