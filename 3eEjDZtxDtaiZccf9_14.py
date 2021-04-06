
def can_play(hand, face):
  if hand == []: return False
  hcols, hnums = zip(*[c.split(" ") for c in hand])
  fcol, fnum = face.split(" ")
  return fcol in hcols or fnum in hnums

