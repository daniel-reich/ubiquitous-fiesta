
def number_of_days(coordinate):
  if (abs(coordinate[0])+abs(coordinate[1]))%5==0:
    return (abs(coordinate[0])+abs(coordinate[1]))+(abs(coordinate[0])+abs(coordinate[1]))//5-1
  else:
    return (abs(coordinate[0])+abs(coordinate[1]))+(abs(coordinate[0])+abs(coordinate[1]))//5

