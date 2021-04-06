
def alternating_caps(txt):
  x = ''
  txt = txt.replace(' ', '  ')
  for i in range(len(txt)):
    if i % 2 == 0:
      x += txt[i].upper()
    else:
      x += txt[i].lower()
  return x.replace('  ', ' ')

