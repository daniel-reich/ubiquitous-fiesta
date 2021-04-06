
def sort_it(lst):
  tp = [[x,x] if isinstance(x, int) else [x,x[0]] for x in lst]
  ls = sorted(tp, key= lambda x : x[1])
  return [x[0] for x in ls]

