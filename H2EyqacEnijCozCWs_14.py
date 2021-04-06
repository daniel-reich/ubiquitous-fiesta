
def first_n_vowels(txt, n):
  vows = "aeiou"
  res = ""
  for c in txt:
    if c in vows:
      res += c
    if len(res) == n:
      return res
  return "invalid"

