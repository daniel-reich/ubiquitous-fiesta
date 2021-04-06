
def reorder_digits(lst, direction):
  if direction == 'asc':
    return [int(''.join(sorted(str(i)))) for i in lst]
  return [int(''.join(sorted(str(i), reverse = True))) for i in lst]

