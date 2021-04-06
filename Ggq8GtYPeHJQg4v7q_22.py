
def replace_vowels(txt, ch):
  x = []
  for i in txt:
    if i in 'aeiou':
      x += [ch]
    else:
      x += [i]
  return ''.join(x)

