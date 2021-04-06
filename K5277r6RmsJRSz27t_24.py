
def emphasise(txt):
  splittxt = txt.split(' ')
  em = []
  if txt == '':
    return ''
  for x in splittxt:
    em.append(x[0].upper() + x[1:].lower())
  return ' '.join(em)

