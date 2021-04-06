
def switches(n):
  if n<3:
    return n
  else:
    return 2**(n-1)+switches(n-2)

