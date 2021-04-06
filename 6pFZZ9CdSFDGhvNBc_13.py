
def factor_group(num):
  for i in range(1, 20):
    if i**2 == num:
      return 'odd'
  return 'even'

