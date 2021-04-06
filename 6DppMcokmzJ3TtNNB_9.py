
def true_alphabetic(txt):
  a = list(txt)
  b = sorted(c for c in a if c.isalpha())
  j = 0
  for i,c in enumerate(a):
    if c.isalpha():
      a[i] = b[j]
      j += 1
  return "".join(a)

