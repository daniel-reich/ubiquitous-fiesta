
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  if pin.isdigit() and len(pin) == 4:
    size = len(moves)
    dancemoves = []
    count = 0
    for s in pin:
      index = (int(s) + count) % size
      dancemoves.append(moves[index])
      count += 1
    return dancemoves
  else:
    return "Invalid input."

