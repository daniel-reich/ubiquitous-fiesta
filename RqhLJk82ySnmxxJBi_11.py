
def power_morphic(num):
  x = sum(str(num**x).endswith(str(num)) for x in range(2,11))
  if x == 9:
    return "Polymorphic"
  if x == 4:
    return "Quadrimorphic"
  if x == 2:
    return "Dimorphic"
  if x == 1:
    return "Enamorphic"
  if x == 0:
    return "Amorphic"

