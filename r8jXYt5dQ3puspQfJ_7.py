
def is_vowel(v):
  return v.lower() in 'aeiou'
  
def split(txt):
  return "".join(sorted(txt, key = is_vowel, reverse = True))

