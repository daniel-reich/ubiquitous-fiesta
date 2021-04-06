
def last(a, n):
  return "invalid" if n > len(a) else ([] if n == 0 else a[-n::])

