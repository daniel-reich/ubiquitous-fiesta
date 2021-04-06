
def common_elements(lst1, lst2):
  it1, it2 = (i for i in lst1), (i for i in lst2)
  el1, el2 = next(it1, None), next(it2, None)
  common = []
  while None not in (el1, el2):
    if el1 > el2:
      el2 = next(it2, None)
    elif el1 < el2:
      el1 = next(it1, None)
    else:
      common.append(el1)
      el1, el2 = next(it1, None), next(it2, None)
  return common

