
def power_morphic(num):
  types = {0:"Amorphic", 1:"Enamorphic", 2:"Dimorphic", 4:"Quadrimorphic", 9:"Polymorphic"}
  return types[len([a for a in range(2,11) if str(num**a).endswith(str(num))])]

