
def retrieve(txt):
  m = txt.replace('.','')
  n = m.split(' ')
  if txt=='':
    return []
  else:
    return [i.lower() for i in n if i[0].lower() in 'aeiou']

