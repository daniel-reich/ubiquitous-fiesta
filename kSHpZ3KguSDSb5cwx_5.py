
def dance_convert(pin):
  moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step",
            "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
  moves = dict(enumerate(moves))
  if pin.isdigit() and len(pin) == 4:
    dance = []
    for i in range(len(pin)):
      num = int(pin[i]) + i
      if num > 9:
        num -= 10
      dance.append(moves[num])
    return dance
  
  else:
    return 'Invalid input.'

