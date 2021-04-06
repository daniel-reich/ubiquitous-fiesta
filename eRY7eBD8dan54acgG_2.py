
def revert_boolean_list(lst):
  return [int(not x) for x in lst]
​
​
def is_checkerboard(lst):
  ok_first = all(lst[k] != lst[k+1] for k, v in enumerate(lst[0][:-1]))
  return ok_first and all(lst[k] == revert_boolean_list(lst[k+1]) for k, v in enumerate(lst[:-1]))

