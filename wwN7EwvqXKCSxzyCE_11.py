
def reorder_digits(lst, direction):
  x = True if direction == 'desc' else False
  return [int(''.join(sorted([char for char in str(num)], reverse=x))) for num in lst]

