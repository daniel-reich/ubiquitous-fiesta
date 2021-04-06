
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  if (len(pin) != 4 or (not pin.isdigit())):
    return "Invalid input.";
  return [moves[(int(pin[idx]) + idx)%len(moves)] for idx in range(0, len(pin))];

