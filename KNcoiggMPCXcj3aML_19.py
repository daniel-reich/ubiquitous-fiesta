
def number_of_days(coordinate):
  dist = abs(coordinate[0]) + abs(coordinate[1])
  rest = dist // 5
  if dist % 5 == 0:
    rest -= 1
  return dist + rest

