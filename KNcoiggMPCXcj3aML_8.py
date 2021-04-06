
def number_of_days(coordinate):
  x,y = coordinate
  travel = abs(x) + abs(y)
  travel_with_rest = travel + (travel//5)
  if travel%5==0: travel_with_rest-=1
  return travel_with_rest

