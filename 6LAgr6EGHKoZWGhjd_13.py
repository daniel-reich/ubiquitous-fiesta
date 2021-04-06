
def final_direction(initial, turns):
  compass = ['N','E','S','W']
  while compass[0] != initial:
    compass.insert(0,compass.pop(-1))
  for turn in turns:
    if turn == "L":
      compass.insert(0,compass.pop(-1))
    elif turn == "R":
      compass.insert(len(compass),compass.pop(0))
  return compass[0]

