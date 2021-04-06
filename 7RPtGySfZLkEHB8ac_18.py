
def wash_hands(N, nM):
  a=N*nM*21*30//60
  b=N*nM*21*30-N*nM*21*30//60*60
  return "{} minutes and {} seconds".format(a,b)

