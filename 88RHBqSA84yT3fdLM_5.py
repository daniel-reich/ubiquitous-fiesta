
def inator_inator(inv):
  n = len(inv)
  return '{}{} {}000'.format(inv, 'inator' if inv[n-1] not in 'aeiouAEOIU' else '-inator', n)

