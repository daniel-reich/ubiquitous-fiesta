
def wash_hands(N, nM):
  tdays = nM*30
  tsecs = N*21*tdays
  tmins = tsecs/60
  dmins = tmins - int(tmins)
  secs = dmins*60
  return str(int(tmins))+" minutes and "+ str(int(secs)) +" seconds"

