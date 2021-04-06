
def percentage_happy(numbers):
  happy = 0
  for i in range(1,len(numbers) - 1):
    if numbers[i - 1] == numbers[i] or numbers[i] == numbers[i+1]:
      happy += 1
  if numbers[0] == numbers[1]:
    happy += 1
  if numbers[-1] == numbers[-2]:
    happy += 1
  return happy/len(numbers)

