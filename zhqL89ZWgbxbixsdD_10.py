
def is_exact(n, fac=1, i=1):
  # Your recursive implementation of the code.
  return is_exact(n, fac*i, i+1) if fac < n else ([fac, i-1] if fac == n else "Not exact!")

