
def wash_hands(N, nM):
  m,s = divmod(N*nM*30*21,60)
  return "{} minutes and {} seconds".format(m,s)

