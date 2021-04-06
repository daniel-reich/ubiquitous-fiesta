
def is_repeated(strn):
  sl = len(strn)
  for i in range(1, 1+sl//2):
    q, r = divmod(sl, i)
    if r == 0 and strn[:i]*q == strn:
      return q
  return False

