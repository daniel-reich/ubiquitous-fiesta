
import re
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  if len(pin) != 4 or len(re.findall(r"\D", pin)) > 0:
    return "Invalid input."
  return [moves[(i + int(x)) % 10] for i, x in enumerate(pin)]

