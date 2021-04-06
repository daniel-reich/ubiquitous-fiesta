
def wash_hands(N, nM):
  total = 21*N*(nM*30)
  return '{} minutes and {} seconds'.format(round((total-total%60)/60), total%60)

