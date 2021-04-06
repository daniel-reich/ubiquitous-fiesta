
def track_robot(instructions):
  if instructions == []:
    return [0, 0]
  else:
    count_lat = 0
    count_long = 0
    lat = [x for x in instructions if 'right' in x or 'left' in x]
    long = [x for x in instructions if 'up' in x or 'down' in x]
    for x in lat:
      if 'right' in x:
        count_lat += eval(''.join(char for char in x if char.isnumeric()))
      elif 'left' in x:
        count_lat -= eval(''.join(char for char in x if char.isnumeric()))
    for x in long:
      if 'up' in x:
        count_long += eval(''.join(char for char in x if char.isnumeric()))
      elif 'down' in x:
        count_long -= eval(''.join(char for char in x if char.isnumeric()))
    return [count_lat, count_long]

