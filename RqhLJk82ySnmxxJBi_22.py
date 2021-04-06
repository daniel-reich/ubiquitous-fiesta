
def power_morphic(num):
  k = 0
  arr = []
  for i in range(2,10):
    arr.append(num**i)
  for x in arr:
    if str(x).endswith(str(num)):
      k += 1
      
  if k == 8:
    return "Polymorphic"
  elif k == 4:
    return "Quadrimorphic"
  elif k == 2:
    return "Dimorphic"
  elif k == 1:
    return "Enamorphic"
  elif k == 0:
    return "Amorphic"

