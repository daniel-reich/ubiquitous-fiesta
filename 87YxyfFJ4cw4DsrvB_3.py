
def generate_rug(n):
  rug = [[0 for i in range(n)] for j in range(n)]
  for x in range(1, int((n - 1) / 2) + 1):
    rug[int(n / 2) + x] = rug[int(n / 2) - x] = [x for y in range(n)]
    for i in range(n):
      rug[i][int(n / 2) + x] = rug[i][int(n / 2) - x] = x
  return rug

