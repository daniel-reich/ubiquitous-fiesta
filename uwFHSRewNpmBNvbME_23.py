
def same_vowel_group(w):
  vwls = lambda a: set(cr for cr in a if cr in "aeiou")
  return [el for el in w if vwls(el) == vwls(w[0])]

