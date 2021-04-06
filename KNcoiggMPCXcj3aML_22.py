
def number_of_days(coordinate):
  res = abs(coordinate[0]) + abs(coordinate[1])
  return res + (res-1)//5

