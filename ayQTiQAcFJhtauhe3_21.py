
def even_or_odd(lst):
  sum = 0
  for n in lst:
    sum += n
  if sum % 2 == 1:
    return 'odd'
  else:
    return 'even'

