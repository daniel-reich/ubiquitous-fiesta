
def portion_happy(numbers):
  happy = (numbers[0] == numbers[1])
  happy += (numbers[-1] == numbers[-2])
  
  for n in range(1,len(numbers)-1):
    happy += (numbers[n-1] == numbers[n]) or (numbers[n+1] == numbers[n])
    
  return happy/len(numbers)

