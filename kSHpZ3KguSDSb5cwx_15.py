
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  dance = []
  for i in range(len(pin)):
    if pin[i].isdigit() and len(pin) == 4:
      if (i + int(pin[i])) < len(moves):
        dance.append(moves[i + int(pin[i])])
      else:
        dance.append(moves[(i + int(pin[i])) - len(moves)])
    else:
      return "Invalid input."
      break
  return dance

