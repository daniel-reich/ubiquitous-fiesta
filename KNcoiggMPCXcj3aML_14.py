
def number_of_days(coordinate):
  total = abs(coordinate[0]) + abs(coordinate[-1])
  if total % 5 == 0:
    extra = total // 5 - 1
  else:
    extra = total // 5
  return total + extra

