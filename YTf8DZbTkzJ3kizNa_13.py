
def moran(n):
  div = 0
  for k in str(n):
    div += int(k)
  if (n/div)%1 != 0:
    return "Neither"
  else:
    res = n//div
    for i in range(2,res):
      if (res % i) == 0:
        return "H"
    else:
      return "M"

