
def track_robot(instructions):
  if instructions == []:
    return [0,0]
  num = []
  x,y = 0,0
  for i in instructions:
    dire,num = i.split(' ')
    if dire == 'left':
      x -= int(num)
    elif dire == 'right':
      x += int(num)
    elif dire == 'up':
      y += int(num)
    else:
      y -= int(num)
  return [x,y]

