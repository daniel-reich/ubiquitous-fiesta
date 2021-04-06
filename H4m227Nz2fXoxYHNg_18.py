
def list_values_types(lst):
  o = []
  for i in lst:
    t = str(type(i))
    lt = t.find("'")
    rt = t.rfind("'")
    o.append(t[lt+1:rt])
  return o

