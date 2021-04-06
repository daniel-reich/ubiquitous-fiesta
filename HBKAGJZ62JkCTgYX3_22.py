
def last(a, n):
  m=len(a)-n
  if n==0:
    return []
  elif m<0:
    return "invalid"
  elif m>=0:
    return a[m:]

