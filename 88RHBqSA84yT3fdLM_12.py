
def inator_inator(inv):
  return inv + 'inator ' + str(len(inv)) + '000' if inv[-1] not in 'aeiouAEIOU' else inv + '-inator ' + str(len(inv)) + '000'

