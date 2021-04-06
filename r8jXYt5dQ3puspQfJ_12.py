
def split(txt):
  vow = ''
  cons = ''
  def is_vowel(c):
    if c in ('aeiou'):
      return True
  for c in txt:
    if is_vowel(c):
      vow += c
    else:
      cons += c
  return vow + cons

