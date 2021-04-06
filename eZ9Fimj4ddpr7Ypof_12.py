
def mumbling(s):
  A=[(s[i]*(i+1)).capitalize() for i in range(len(s))]
  return '-'.join(A)

