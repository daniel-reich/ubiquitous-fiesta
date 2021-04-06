
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  if pin.isnumeric() and len(pin) == 4:
    return [moves[(index+int(num))% len(moves)] for index,num in enumerate(pin)]
  return "Invalid input."

