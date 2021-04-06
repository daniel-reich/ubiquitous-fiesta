
from itertools import chain
def num_then_char(lst):
  len_list = [len(i) for i in lst]
  unp_list = list(chain.from_iterable(lst))
  sorted_list = sorted(i for i in unp_list if type(i) in (int, float)) \
          + sorted(i for i in unp_list if type(i) == str)
  result = []
  for i in len_list:
    add_list = []
    for _ in range(i):
      add_list.append(sorted_list.pop(0))
    result.append(add_list)
  return result

