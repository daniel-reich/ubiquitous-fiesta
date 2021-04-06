
def is_equal(lst):
  new_lst = list(map(lambda n: sum([int(x) for x in str(n)]), lst))
  return new_lst[0] == new_lst[1]

