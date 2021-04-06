
def is_exact(n,f=[1]):
  if n>f[-1]:
    f+=[len(f)*f[-1]]
    return is_exact(n,f)
  return n in f and [n,f.index(n)] or "Not exact!"

