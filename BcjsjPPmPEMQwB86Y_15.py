
cons = "bcdfghjklmnpqrstvwxyz"
def slicer(w):
  l = len(w)
  return {w[i:i+s] for s in range(1,l+1) for i in range(l-s+1)}
​
def get_vowel_substrings(txt):
  return sorted(x for x in slicer(txt) if x[0] in "aeiou" and x[-1] in "aeiou")
​
def get_consonant_substrings(txt):
  return sorted(x for x in slicer(txt) if x[0] in cons and x[-1] in cons)

