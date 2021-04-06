
def reorder_digits(lst, direction):
  return [int(''.join(sorted(str(l), reverse=True))) if direction == 'desc' else int(''.join(sorted(str(l)))) for l in lst]

