
def final_direction(initial, turns):
  com = ["N", "E", "S", "W"]  # The directions on a compass in order
  overall_turn = 0
  initial_pos = com.index(initial)  # The position of the initial position
  
  for l in turns:  # Counting the tunrs
    if l == "R":
      overall_turn += 1
    else:
      overall_turn -= 1
    
  index = ((overall_turn + initial_pos) % 4)  # Using modulo to keep it in range and get the total displacement
  
  return com[index]

