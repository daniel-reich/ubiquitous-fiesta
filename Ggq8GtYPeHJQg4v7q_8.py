
def replace_vowels(txt, ch):
  return''.join([ch if i in list('aeiouAEIOU') else i for i in txt])

