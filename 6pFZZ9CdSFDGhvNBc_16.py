
def factor_group(num):
  cnt = 0
  
  for i in range(1, num+1):
    if num % i == 0:
      cnt += 1
  
  return "even" if cnt % 2 == 0 else "odd"

