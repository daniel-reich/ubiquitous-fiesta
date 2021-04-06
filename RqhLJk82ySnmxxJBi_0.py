
def power_morphic(num):
  morphic = {9:"Polymorphic", 4:"Quadrimorphic", 2:"Dimorphic", 1:"Enamorphic"}
  n = sum(str(num**i).endswith(str(num)) for i in range(2,11))
  return morphic.get(n, "Amorphic")

