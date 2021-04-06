
def vow_replace(word, vowel):
  a = word.replace("a", vowel)
  e = a.replace("e", vowel)
  i = e.replace("i", vowel)
  o = i.replace("o", vowel)
  u = o.replace("u", vowel)
  return u

