
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  newpin = []
  if len(pin) != 4:
    return "Invalid input."
  for i,v in enumerate(pin):
    if v not in "0123456789":
      return "Invalid input."
    
    index = int(i)+int(v)
    print(index)
    if index > 9:
      index -= 10
    newpin.append(moves[index])
  return newpin

