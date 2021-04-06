
def safecracker(start, increments):
  curr = start
  sgn = -1
  result = []
  while len(increments) > 0:
    curr = (curr + sgn * increments.pop(0)) % 100
    result.append(curr)
    sgn *= -1
  return result

