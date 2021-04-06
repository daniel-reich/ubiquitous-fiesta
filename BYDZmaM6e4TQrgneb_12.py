
def fib_fast(num):
  f_n2 = 0
  f_n1 = 1
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    for i in range(2, num+1):
      sum = f_n1 + f_n2
      f_n2 = f_n1
      f_n1 = sum
  return sum

