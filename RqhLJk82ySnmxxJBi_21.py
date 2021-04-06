
def power_morphic(num):
  count = sum(str(pow(num, exp)).endswith(str(num)) for exp in range(2, 10))
  dct = {8: "Polymorphic", 4: "Quadrimorphic", 2: "Dimorphic",
         1: "Enamorphic", 0: "Amorphic"}
  return dct[count]

