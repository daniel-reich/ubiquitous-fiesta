
def portion_happy(numbers):
  happy=0
  if numbers[0]==numbers[1]: happy+=1
  if numbers[-1]==numbers[-2]: happy+=1
  for i in range(1,len(numbers)-1):
    if numbers[i]==numbers[i-1] or numbers[i]==numbers[i+1]: happy+=1
  return happy/len(numbers)

