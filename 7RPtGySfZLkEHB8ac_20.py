
def wash_hands(N, nM):
  total_seconds = (N * 21) * (nM * 30)
  minutes = int(total_seconds / 60)
  seconds = int(total_seconds % 60)
  return str(minutes) + " minutes and " + str(seconds) + " seconds"

