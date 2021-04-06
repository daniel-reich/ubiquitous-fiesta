
def lcm_three(num):
  num1, num2, num3 = sorted(num)
  current_num = num3
  while not ((current_num % num1 == 0) and (current_num % num2 == 0)):
    current_num += num3
  return current_num

