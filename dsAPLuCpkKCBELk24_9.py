
def get_products(lst):
  ret = []
  for i in range(0,len(lst)):
    nl = lst.copy()
    nl.pop(i)
    total = 1
    for l in nl:
      total *= l
    ret.append(total)
  return ret

