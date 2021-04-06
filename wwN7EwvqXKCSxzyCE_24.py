
def reorder_digits(lst, direction):
  for idx, num in enumerate(lst):
    num = list(str(num))
    if direction == 'desc':
      num.sort(key=int, reverse=True)
    else:
      num.sort(key=int)
    num = int(''.join(num))
    lst[idx] = num
  return lst

