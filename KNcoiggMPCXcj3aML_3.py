
def number_of_days(coordinate):
  d = abs(coordinate[0]) + abs(coordinate[1])
  return d + d // 5 + (-1 if d % 5 == 0 else 0)

