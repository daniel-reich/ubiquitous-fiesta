
def power_morphic(num):
  count = 0
  d = {9:"Polymorphic",4:"Quadrimorphic",2:"Dimorphic",1:"Enamorphic", 0:"Amorphic"}
  for i in range(2,11):
    if str(num**i)[-len(str(num)):]  == str(num):
      count += 1
  return d[count]

