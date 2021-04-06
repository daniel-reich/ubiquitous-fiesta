
def is_apocalyptic(number):
  e = str(2 ** number)
  f = ''.join(e.split('666'))
  c = (len(e) - len(f)) // 3
  if c == 0:
    return 'Safe'
  elif c == 1:
    return 'Single'
  elif c == 2:
    return 'Double'
  elif c == 3:
    return 'Triple'
  else:
    return '>3'

