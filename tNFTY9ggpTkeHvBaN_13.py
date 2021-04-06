
def total_volume(*boxes):
  total = 0
  for i in boxes:
    suma = 1
    for j in range(0, len(i)):
      suma *= i[j] 
    total += suma
  
  return total

