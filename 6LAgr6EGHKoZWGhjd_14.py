
def final_direction(initial, turns):
  compass = ["N", "E", "S", "W"]
  pointer = 0
  for direction in turns:
    if direction == "R":
      pointer += 1
    else:
      pointer -= 1
      
  initial_idx = compass.index(initial)
  return compass[(initial_idx + pointer) % 4]

