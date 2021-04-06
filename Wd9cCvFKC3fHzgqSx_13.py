
def num_split(num):
  if abs(num) < 10:
    return [num]
  if num < 0:
    k = -1
  else:
    k = 1
  return list(map(lambda x: k * 10 * x, num_split(abs(num) // 10))) + [k * (abs(num) % 10)]

