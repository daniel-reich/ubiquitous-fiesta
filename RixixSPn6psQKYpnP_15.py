
def mystery_func(lst, n):
  return_lst = []
  for i in range(len(lst)):
    return_lst.append(lst[i] % n)
  return return_lst

