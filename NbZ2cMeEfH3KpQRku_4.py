
def percentage_happy(numbers):
  unhappy = sum([
    numbers[i-1:i+2] in [[0,1,0], [1,0,1]]
    for i in range(1, len(numbers)-1)
  ])
  if numbers[0] != numbers[1]:
    unhappy += 1
  if numbers[-1] != numbers[-2]:
    unhappy += 1
    
  return 1.0 - (unhappy / len(numbers))

