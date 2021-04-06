
def does_rhyme(txt1, txt2):
  vowels = set(list('aeiou'))
  a = txt1.lower().split()[-1]
  b = txt2.lower().split()[-1]
  return set(a) & vowels == set(b) & vowels

