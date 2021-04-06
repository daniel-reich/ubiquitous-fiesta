
def max_collatz(num):
  max_num = num
  while num != 1:
    if num % 2 == 0:
      num /= 2
    else:
      num = num * 3 + 1
    
    if num > max_num:
      max_num = num
  return max_num

