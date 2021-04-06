
from collections import Counter as C
def hidden_anagram(text, phrase):
  T=[x for x in text.lower() if x.isalpha()]
  P=[x for x in phrase.lower() if x.isalpha()]
  A=[T[i:i+len(P)] for i in range(0, len(T)-len(P)+1)]
  for x in A:
    if all(y in P for y in x) and C(x)==C(P):
      return ''.join(x)
  return "noutfond"

