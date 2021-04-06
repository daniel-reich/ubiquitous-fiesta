
def first_n_vowels(txt, n):
  res = ''
  for c in txt:
    if c in {'a','e','u','i','o'}:
      res += c
      n -= 1
      if n == 0:
        break
  return "invalid" if n else res

