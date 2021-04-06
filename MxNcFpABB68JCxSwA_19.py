
def legendre(p, n):
  lst = [n//p]
  while lst[-1]: lst += [lst[-1]//p]
  return sum(lst)

