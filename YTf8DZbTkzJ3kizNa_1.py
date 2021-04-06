
def moran(n):
  div = eval("+".join(list(str(n))))
  if n%div == 0:
    for i in range(2,n):
      if (n % i) == 0:
        return "H"
        break
      else:
        return "M"
  else:
    return "Neither"

