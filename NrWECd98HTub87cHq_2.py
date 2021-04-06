
def overlapping_rectangles(rect1, rect2):
  y = 0
  left1 = rect1[0]
  right1 = rect1[0] + rect1[2]
  roof1 = rect1[1] + rect1[3]
  floor1 = rect1[1]
  left2 = rect2[0]
  right2 = rect2[0] + rect2[2]
  roof2 = rect2[1] + rect2[3]
  floor2 = rect2[1]
    
  if right1>left2 and roof1>floor2:
    if left1 > left2:
      left = left1
    else:
      left = left2
​
    if right1 < right2:
      right = right1
    else:
      right = right2
​
    if floor1 > floor2:
      floor = floor1
    else:
      floor = floor2
​
    if roof1 < roof2:
      roof = roof1
    else:
      roof = roof2
  else:
    y = 1
    
  if y == 0:
    area = (roof-floor)*(right - left)
  else: 
    area = 0
  return (area)

