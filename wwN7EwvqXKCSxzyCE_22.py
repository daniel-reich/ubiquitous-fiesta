
def reorder_digits(lst, direction):
  for i in range(len(lst)):
    if direction == 'asc':
      lst[i] = int(''.join(sorted(str(lst[i]), reverse = False)))
    elif direction == 'desc':
      lst[i] = int(''.join(sorted(str(lst[i]), reverse = True)))
  return lst

