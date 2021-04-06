
def perrin(n):
  perrin = [3,0,2]
  for i in range(n - 2):
    perrin.append(perrin[-2]+perrin[-3])
  return perrin[-1]

