
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  newpin = []
  counter = 0
  if len(pin) == 4 and pin.isdecimal():
    for num in pin:
      move = int(num) + counter
      if move > 9:
        move -= 10
      newpin.append(moves[move])
      counter += 1
  else:
    return 'Invalid input.'
  return newpin

