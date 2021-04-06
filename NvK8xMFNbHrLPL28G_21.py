
def highest_digit(num):
  num_list = list(str(num))
  max = 0
  for n in num_list:
    if int(n) > max:
      max = int(n)
  return max

