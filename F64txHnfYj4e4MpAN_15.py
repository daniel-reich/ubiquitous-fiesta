
def schoty(frame):
  return int(''.join(str(s[:s.index("-")].count("O")) for s in frame))

