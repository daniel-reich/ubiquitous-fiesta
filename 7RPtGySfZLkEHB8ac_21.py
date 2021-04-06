
def wash_hands(N, nM):
  total_seconds = 21 * N * 30 * nM
  minutes = total_seconds//60
  seconds = total_seconds - minutes *60
  return "{} minutes and {} seconds".format(minutes, seconds)

