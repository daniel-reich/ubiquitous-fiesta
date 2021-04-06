
def replace_vowels(txt, ch):
  v = ('a', 'e', 'i', 'o', 'u')
  return ''.join([let if let not in v else ch for let in txt])

