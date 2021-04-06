
def first_n_vowels(txt, n):
  k = ""
  for letter in txt:
    if letter in "AEOUIaeiou":
      k += letter
  if n <= len (k):
    return k[:n]
  else:
    return "invalid"

