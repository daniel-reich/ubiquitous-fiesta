
def number_split(n):
  if n&1:
    n += 1
    return [n//2-1,n//2]
  return [n//2,n//2]

