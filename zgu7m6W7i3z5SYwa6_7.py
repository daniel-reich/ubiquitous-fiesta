
def is_equal(lst):
  n_lst = [str(inp) for inp in lst]
  return sum([int(i) for i in n_lst[0]]) == sum([int(i) for i in n_lst[1]])

