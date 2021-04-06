
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  if not pin.isdigit() or len(pin) != 4: return "Invalid input."
  dances = []
  for i in range(len(pin)):
    indx = int(pin[i]) + i
    if  indx > len(moves) - 1: indx = indx - 10
    dances.append(moves[indx])
  return dances

