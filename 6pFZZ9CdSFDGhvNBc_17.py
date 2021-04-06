
def factor_group(num):
  # numbers that are perfect squares have an odd number of factors
  # others have an even number of factors
  i = 1
  while i*i <= num:
    if i*i == num:
      return 'odd'
    i += 1
  return 'even'

