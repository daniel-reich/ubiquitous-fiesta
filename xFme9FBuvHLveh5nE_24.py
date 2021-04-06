
def is_zygodrome(n):
  n = str(n)
  return not 1 in [len(i) for i in "".join([x if x == n[i+1] else x + "." for i, x in enumerate(n[:-1])] + [n[-1]]).split(".")]

