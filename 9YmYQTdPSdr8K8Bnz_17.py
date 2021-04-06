
def unique_lst(lst):
  out = []
  ls3 = [out.append(i) for i in [x for x in lst if x>0] if not out.count(i)]
  return out

