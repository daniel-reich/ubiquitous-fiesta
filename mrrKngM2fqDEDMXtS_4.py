
def can_patch(b, p):
  b = [i for i in map(len,''.join(map(str,b)).split("1")) if i>1]
  while b:
    x = b[0]
    if not (x in p or x-1 in p): return False
    p.remove(x-1 if x-1 in p else x); b.pop(0)
  return True

