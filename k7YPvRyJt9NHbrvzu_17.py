
points = [2,3,6,7,8]
def football(score, series = [[]], pointer = 0):
  if pointer == len(points):
    return len([serie for serie in series if sum(serie) == score])
  point = points[pointer]
  limit = score // point + 1
  series = [serie + [point]*i for i in range(limit) for serie in series]
  return football(score, series, pointer +1)

