
def power_morphic(num):
  classification = {9: "Polymorphic", 
          4: "Quadrimorphic",
          2: "Dimorphic",
          1: "Enamorphic",
          0: "Amorphic"}
  powers = [str(num**i)[-len(str(num)):] for i in range(2,11)]
  
  return classification[powers.count(str(num))]

