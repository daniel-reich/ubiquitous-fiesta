
def safecracker(start, increments):
  k = []
  k.append((start-increments[0])%100)
  k.append((start-increments[0]+increments[1])%100)
  k.append((start-increments[0]+increments[1]-increments[2])%100)
  return k

