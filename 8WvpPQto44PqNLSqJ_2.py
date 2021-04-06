
def pad(m):
  l = len(m)
  if l==140: return m
  return m + " "*(l%2==0) + "l" + "ol"*((138-l+l%2)//2)

