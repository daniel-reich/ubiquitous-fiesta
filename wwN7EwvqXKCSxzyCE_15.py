
def reorder_digits(lst, direction):
  if direction == 'desc':
    return [int(''.join(sorted(str(num), reverse=True))) for num in lst]
  else:
    return [int(''.join(sorted(str(num)))) for num in lst]

