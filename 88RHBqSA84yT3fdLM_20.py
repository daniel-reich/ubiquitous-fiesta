
def inator_inator(inv):
  if inv[-1].lower() in 'aeiou':
    return inv + '-inator ' + str(len(inv)) + '000'
  return inv + 'inator ' + str(len(inv)) + '000'

