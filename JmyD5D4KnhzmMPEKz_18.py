
from string import ascii_lowercase as alphabet
​
def constraint(txt):
  txt = txt.lower()
  words = txt.split()
  if all(ch in txt for ch in alphabet):
    return 'Pangram'
  if all(txt.count(ch) == 1 for ch in txt if ch.isalpha()):
    return 'Heterogram'
  if all(w[0] == txt[0] for w in words):
    return 'Tautogram'
  if any(all(ch in w for w in words) for ch in txt):
    return 'Transgram'
  return 'Sentence'

