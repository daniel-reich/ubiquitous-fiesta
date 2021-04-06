
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  if not pin.isdigit() or len(pin) != 4:
    return "Invalid input."
  return [moves[(i+int(pin[i]))%10] for i in range(len(pin))]

