
def is_positive_dominant(lst):
  return sum(1 if i>0 else -1 for i in set(lst) if i!=0)>0

