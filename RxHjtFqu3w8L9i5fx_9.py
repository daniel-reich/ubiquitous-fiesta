
def bell(n):
  lst = [1]
  for i in range(n-1):
    new_lst = [lst[-1]]
    for j, v in enumerate(lst):
      new_lst.append(v + new_lst[-1])
    lst = new_lst
  return lst[-1]

