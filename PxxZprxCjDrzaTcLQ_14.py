
def vowel_links(txt):
  txt, vow = txt.split(), 'aeiou'
  return any(x[-1] in vow and y[0] in vow for x, y in zip(txt, txt[1:]))

