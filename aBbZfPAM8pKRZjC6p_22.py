
def fruit_salad(fruits):
  fruitsalad = []
  for fruit in fruits:
  
    length = len(fruit)
    left = fruit[0:int(length/2)]
    right = fruit[int(length/2):]
    fruitsalad.append(left)
    fruitsalad.append(right)
    fruitsalad = sorted(fruitsalad)
    
  return "".join(fruitsalad)

