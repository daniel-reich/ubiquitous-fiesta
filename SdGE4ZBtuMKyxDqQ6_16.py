
def first_repeat(chars):
  y = ''
  b = ''
  for x in chars:
    if x in y:
      b +=x
    else:
      y += x
  if b == '':
    return '-1'
  return b[0]

