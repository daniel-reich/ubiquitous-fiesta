
#A 1 is unhappy if the digit to its left and the digit to 
#its right are both 0s. A 0 is unhappy if the digit to 
#its left and the digit to its right are both 1s. 
#If a number has only one neighbor, it is unhappy 
#if its only neighbor is different. Otherwise, 
#a number is happy.
​
def percentage_happy(numbers):
  h = 0
  t = 0
  for i in range(0, len(numbers)):
    t += 1
    if i == 0:
      if numbers[i] == numbers[i+1]:
        h += 1
    elif i == len(numbers) - 1:
      if numbers[i-1] == numbers[i]:
        h += 1
    else:
      if numbers[i-1] == numbers[i] or numbers[i] == numbers[i+1]:
        h += 1
  return h/t

