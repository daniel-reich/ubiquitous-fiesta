
def vowel_links(txt):
  txt = txt.split()
  return any(x[-1] in 'aeiou' and y[0] in 'aeiou' for x, y in zip(txt, txt[1:]))

