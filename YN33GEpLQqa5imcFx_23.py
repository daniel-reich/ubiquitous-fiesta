
def pascals_triangle(row):
  lst = [[1,1]]
  while len(lst) < row:
    lst.append(new_row(lst[-1]))
  return ' '.join([str(i) for i in lst[-1]])
  
def new_row(lst):
  new_lst = [1]
  for i in range(len(lst)-1):
    new_lst.append(lst[i]+lst[i+1])
  new_lst.append(1)
  return new_lst

