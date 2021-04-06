
def number_of_days(coordinate):
  distance = sum(abs(i) for i in coordinate)
  return distance + distance//5 - (1 if not distance%5 else 0)

