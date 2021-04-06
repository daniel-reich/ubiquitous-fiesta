
def verbify(txt):
  splitted_text = txt.split()
  if splitted_text[0][-1] == 'e':
    splitted_text[0] = ''.join([splitted_text[0], 'd'])
  elif splitted_text[0][-2:] != 'ed':
    splitted_text[0] = ''.join([splitted_text[0], 'ed'])
  return ' '.join(splitted_text)

