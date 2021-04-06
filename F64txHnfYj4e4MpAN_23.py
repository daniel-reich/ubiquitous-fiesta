
def schoty(frame):
  return sum(e.find('-') * 10 ** i for i,e in enumerate(frame[::-1]))

