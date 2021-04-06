
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  if len(pin) != 4 or [d for d in pin if not d.isdigit()]:
    return "Invalid input."
  else:
    move_list = []
    for i in range(4):
      this_move = i + int(pin[i])
      if this_move > 9:
        this_move -= 10
      move_list.append(moves[this_move])
  return move_list

