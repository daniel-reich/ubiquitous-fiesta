
def list_operation(x, y, n):
  new_list = range(x,y+1)
  sort_list = []
  for i in new_list:
    if i%n == 0:
      sort_list.append(i)
  return sort_list

