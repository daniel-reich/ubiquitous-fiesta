
def list_to_string(lst):
  lst2 = []
  for n in lst:
    lst2.append(str(n))
  tpl = tuple(lst2)
  x = ''.join(tpl)
  return x

