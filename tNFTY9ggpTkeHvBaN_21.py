
def total_volume(*boxes):
  sum = 0
  
  for i in boxes:
    product = 1
    curr = i
    for j in curr:
      product *= j
      
    sum += product
    
  return sum

