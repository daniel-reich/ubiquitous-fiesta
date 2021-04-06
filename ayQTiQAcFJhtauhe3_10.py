
def even_or_odd(lst):
  count = 0
  for num in lst:
    count += num
  if count % 2 == 1:
    return 'odd'
  return 'even'

