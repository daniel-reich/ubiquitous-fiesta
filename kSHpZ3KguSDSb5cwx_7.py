
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  if not pin.isdigit() or len(str(pin)) !=4:
    return 'Invalid input.'
  return [moves[(int(i) + idx) % 10] for idx,i in enumerate(str(pin))]

