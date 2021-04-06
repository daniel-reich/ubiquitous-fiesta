
def staircase(n, p = 0, res = ""):
  if n > 0:
    if p == n - 1:
      return "_"*p + "#" + res
    return staircase(n, p+1, "\n"+ "_"*p + "#"*(n-p) + res)
  if p == abs(n)-1:
    return  "#"*(p+1) + res
  return staircase(n, p+1, "\n"+ "_"*(abs(n)-p-1) + "#"*(p+1) + res)

