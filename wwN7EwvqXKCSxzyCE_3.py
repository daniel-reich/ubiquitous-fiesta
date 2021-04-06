
def reorder_digits(lst, direction):
  new_lst = []
  for i in lst:
    num = ''.join(sorted(str(i)))
    if direction == 'asc':
      new_lst.append(int(num))
    else:
      new_lst.append(int(num[::-1]))
  return new_lst

