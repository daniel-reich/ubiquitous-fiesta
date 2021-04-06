
def factor_group(num):
  count = 0
  for i in range(1,num+1):
    if num % i == 0:
      count += 1
  return 'even' if count % 2 == 0 else 'odd'

