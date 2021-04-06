
def first_n_vowels(txt, n):
  res, count = "", 0
  for l in txt:
    if count == n: return res
    if l in "aeiou": 
      res += l
      count += 1
  return "invalid"

