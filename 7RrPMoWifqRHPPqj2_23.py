
def safecracker(start, increments):
  v1 = start - increments[0]
  if v1 < 0:
    v1 = 100 + v1
  v2 = v1 + increments[1]
  if v2 > 99:
    v2 = v2 - 100
  v3 = v2 - increments[2]
  if v3 < 0:
    v3 = 100 + v3
  return [v1, v2, v3]

