
def wash_hands(N, nM):
  minutes = (((N*21)*30)*nM)//60
  seconds = (((N*21)*30)*nM)%60
  return str(minutes) + " minutes and " + str(seconds) + " seconds"

