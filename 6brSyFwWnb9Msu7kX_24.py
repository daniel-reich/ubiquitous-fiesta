
def pos_neg_sort(lst):
  p=sorted(list(filter(lambda x:x>0,lst)))
  return [i if i<0 else p.pop(0) for i in lst]

