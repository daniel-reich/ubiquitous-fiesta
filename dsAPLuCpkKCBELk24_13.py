
def get_products(lst):
  from functools import reduce
  result = []
  for i in lst:
    temp_lst = lst.copy()
    temp_lst.remove(i)
    c = reduce(lambda x, y: x*y, temp_lst)
    result.append(c)
  return result

