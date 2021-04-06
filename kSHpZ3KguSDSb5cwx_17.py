
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  
  if len(pin) == 4:
  
    try:
      return [moves[int(pin[i]) + i] if (int(pin[i]) + i) < 10 else moves[int(pin[i]) + i - 10] for i in range(len(pin))]
  
    except ValueError:
      return "Invalid input."
  
  else:
    return "Invalid input."

