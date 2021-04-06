
def final_direction(initial, directions):
  d = {'N' : 90, 'E' : 0, 'S' : 270, 'W' : 180}
​
  degree = d[initial]
  for direction in directions:
    if direction == 'L':
      degree += 90 
    else:
      degree -= 90 
  while degree < 0:
    degree += 360
  while degree >= 360:
    degree -= 360
  
  for k, v in d.items():
    if v == degree:
      return k

