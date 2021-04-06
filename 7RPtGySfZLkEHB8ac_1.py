
def wash_hands(N, nM):
  sec = N*21*nM*30
  return '{} minutes and {} seconds'.format(sec//60, sec%60)

