
def reorder_digits(lst, direction):
  new_lst=[]
  for i in lst:
    if direction=='asc':
      new_lst.append(int(''.join(sorted(str(i)))))
    if direction=='desc':
      new_lst.append(int(''.join(sorted(str(i),reverse=True))))
  return new_lst

