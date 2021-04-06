
def number_of_days(coordinate):
  travel_days = sum([abs(coor) for coor in coordinate])
  rest_days = (travel_days // 5)
​
  if travel_days % 5 == 0:
    rest_days -= 1
​
  return travel_days+rest_days

