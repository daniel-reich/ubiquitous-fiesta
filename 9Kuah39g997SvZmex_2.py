
def common_last_vowel(txt):
  for c in txt.lower()[::-1]:
    if c in "aeuio":
      return c

