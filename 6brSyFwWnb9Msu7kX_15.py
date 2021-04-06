
def pos_neg_sort(lst):
  pos = sorted([x for x in lst if x>0])
  return [pos.pop(0) if x>0 else x for x in lst]

