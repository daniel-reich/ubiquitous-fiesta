
def is_happy(n, traversed = None):
  if traversed is None:
    traversed = set()
  n = sum(int(d)**2 for d in str(n))
  if n==1:
    return True
  if n in traversed:
    return False
  traversed.add(n)
  return is_happy(n, traversed)

