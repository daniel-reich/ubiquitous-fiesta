
def true_alphabetic(txt):
  sort = sorted(txt.replace(' ', ''))
  out = ''
  for letter in txt:
    if letter == ' ':
      out += ' '
    else:
      out += sort.pop(0)
  return out

