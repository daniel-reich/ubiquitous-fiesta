
def factor_group(num):
  x = len([i for i in range(1, num + 1) if num % i == 0])
  if x % 2 == 0:
    return 'even'
  return 'odd'

