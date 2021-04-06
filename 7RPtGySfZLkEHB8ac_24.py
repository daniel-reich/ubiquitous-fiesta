
def wash_hands(N, nM):
  day = 21*N
  mth = day*30
  dur = mth*nM
  mins = dur // 60
  dur -= (mins * 60)
  if dur:
    secs = dur
  else:
    secs = 0
  return "{} minutes and {} seconds".format(mins, secs)

