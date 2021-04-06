
def safecracker(start, increments):
  return [(start-increments[0])%100,(start-increments[0]+increments[1])%100,(start-increments[0]+increments[1]-increments[2])%100]

