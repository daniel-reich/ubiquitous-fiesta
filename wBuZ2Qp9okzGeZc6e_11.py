
def first_place(road):
  car = ''
  if len(road) == road.count('=') or len(road) == 0:
    return None
  else:
    for x in road:
      if x != '=':
        car = '{}'.format(x)
  return car

