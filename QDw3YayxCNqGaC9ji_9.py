
def make_change(c):
  q = c//25
  qr = c%25
  d = qr//10
  dr = qr%10
  n = dr//5
  nr = dr%5
  p = dr%5
  return {"q":q,"d":d,"n":n,"p":p}

