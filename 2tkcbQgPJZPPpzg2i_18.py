
def sum_of_holes(N):
  numHoles = 0
  holes = {
  0 : 1,
  4 : 1,
  6 : 1,
  8 : 2,
  9 : 1
  }
  for i in range(N):
    for j in str(i+1):
      numHoles += holes.get(int(j), 0)
  return numHoles

