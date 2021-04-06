
def sort_array(lst):
  if len(lst) < 2: return lst
  return sort_array([x for x in lst if x<lst[0]]) + [x for x in lst if x==lst[0]] + sort_array([x for x in lst if x>lst[0]])

