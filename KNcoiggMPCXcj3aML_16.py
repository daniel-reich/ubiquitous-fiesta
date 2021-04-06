
def number_of_days(coordinate):
  d = abs(coordinate[0]) + abs(coordinate[1])
  if d < 5:
    return d
  else :
    return d + int((d-1)/5)

