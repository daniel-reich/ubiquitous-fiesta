
compass = {'N':0, 'E':90, 'S':180, 'W':270, 'R':90, 'L':-90, 0:'N', 90:'E', 180:'S', 270:'W'}
​
def final_direction(initial, turns):
  direction = compass[initial]
  for turn in turns:
    direction += compass[turn]
  direction = direction % 360
  return compass[direction]

