
def number_of_repeats(s):
  sl = len(s)
  for l in range(2, 1+sl//2):
    nr, r = divmod(sl, l)
    if not r and s[:l]*nr == s:
      return nr
  return 1

