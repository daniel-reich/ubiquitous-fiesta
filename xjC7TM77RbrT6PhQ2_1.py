
def switches(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  else:
    return switches(n-1)+2*switches(n-2) + 1

