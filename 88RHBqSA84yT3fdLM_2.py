
def inator_inator(inv):
  if inv[-1].lower() not in ['a', 'e', 'i', 'o', 'u']:
    return inv + 'inator ' + str(len(inv)) + '000'
  else:
    return inv + '-inator ' + str(len(inv)) + '000'

