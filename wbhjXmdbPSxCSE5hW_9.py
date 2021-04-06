
def sigilize(desire):
  txt = ''
  for ch in desire.upper().replace(' ', '')[::-1]:
    if ch not in txt and ch not in 'AEIOU':
      txt += ch
  return txt[::-1]

