
def common_elements(lst1, lst2):
  return [k for k in sorted(list(set(lst1))) if k in lst2]

