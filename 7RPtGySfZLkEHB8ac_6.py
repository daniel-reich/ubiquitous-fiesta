
def wash_hands(N, nM):
  seconds = N * nM * 30 * 21
  return '{} minutes and {} seconds'.format(seconds//60,seconds%60)

