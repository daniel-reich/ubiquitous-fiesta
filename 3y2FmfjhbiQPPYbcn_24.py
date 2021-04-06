
def pop(s):
  for i in range(len(s)//2):s[i]=s[-i-1]=i
  return s

