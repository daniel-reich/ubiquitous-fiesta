
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
import re
def dance_convert(pin):
  if re.search('\d{4}', pin) == None:
    return 'Invalid input.'
  else:
    return [moves[(int(pin[x]) + x) % (len(moves))] for x in range(len(pin))]

