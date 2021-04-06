
def wash_hands(N, nM):
  #wash = 21 seconds
  n_ = (N * 21) * 30 * nM
  return str((n_ // 60)) + " minutes and " + str((n_ % 60)) + " seconds"

