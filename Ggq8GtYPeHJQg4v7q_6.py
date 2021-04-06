
def replace_vowels(txt, ch):
  vows = ('a', 'e', 'i', 'o', 'u')
  return ''.join([ch if l in vows else l for l in txt])

