
def replace_vowels(txt, ch):
  vowels = "aeiou"
  new = [ ch if x in vowels else x for x in txt  ]
  return ''.join(new)

