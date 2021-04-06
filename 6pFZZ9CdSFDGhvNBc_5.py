
def factor_group(num):
  count = 0
  for ix in range(num):
    if num % (ix + 1) == 0:
      count += 1
  if count % 2 == 0:
    return 'even'
  else:
    return 'odd'

