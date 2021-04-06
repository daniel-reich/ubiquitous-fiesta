
def will_hit(trajectory, location):
  data = trajectory.split('=')[1].split('x')
  x =  int(data[0].strip())
  y_with_sign = data[1][1:].split(' ')
  if '-' in y_with_sign[0]:
      y = -int(y_with_sign[1])
  else:
      y = int(y_with_sign[1])
​
  return True if location[0]*x + y == location[1] else False

