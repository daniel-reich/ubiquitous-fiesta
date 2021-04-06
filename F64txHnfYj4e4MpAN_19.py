
def schoty(frame):
  m, v = len(frame) - 1, 0
  for i in frame:
    v += 10 ** m * i.find('-')
    m -= 1
  return v

