
def mystery_func(num):
  numbers = []
  sum_numbers = 1
  while sum_numbers <= num:
    numbers.append(2)
    sum_numbers = sum_numbers * 2
    
  sum_numbers = sum_numbers / 2
  numbers = numbers[1:]
  numbers.append(int(num - sum_numbers))
  
  result = ""
  for i in numbers:
    result = result + str(i)
  
  return int(result)

