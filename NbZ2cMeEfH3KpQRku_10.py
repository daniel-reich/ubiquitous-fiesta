
def portion_happy(numbers):
  unhap = 0
  if numbers[0] != numbers[1]:
    unhap += 1
  if numbers[-1] != numbers[-2]:
    unhap += 1
  for i in range(1, len(numbers)-1):
    if numbers[i-1] == numbers[i+1]:
      if numbers[i-1] != numbers[i]:
        unhap += 1
  return (len(numbers)-unhap)/len(numbers)

