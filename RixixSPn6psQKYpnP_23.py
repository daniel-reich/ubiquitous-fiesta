
def mystery_func(lst, n):
  new_lst = []
  for i in lst:
    new_lst.append(i%n)
  return new_lst

