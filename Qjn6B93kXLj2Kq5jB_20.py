
def simplify_frac(f):
  first = int(f[:f.index("/")])
  second = int(f[f.index("/")+1:])
  i = first
  while i > 0:
    if first % i == 0 and second % i == 0:
      first /= i
      second /= i
    i -= 1
  return str(int(first)) + "/" + str(int(second))

