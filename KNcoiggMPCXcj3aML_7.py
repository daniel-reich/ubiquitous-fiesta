
def number_of_days(coordinate):
  if abs(sum(coordinate)) % 5 == 0:
    return abs(sum(coordinate)) + abs(sum(coordinate))//5-1
  else:
    return  abs(sum(coordinate)) + abs(sum(coordinate))//5

