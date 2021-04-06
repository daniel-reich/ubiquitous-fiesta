
def repeated(s):
  return any(s[:k]*(len(s)//k)==s for k in range(1,1+len(s)//2))

