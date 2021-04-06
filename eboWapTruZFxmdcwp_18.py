
def is_positive_dominant(lst):
  return sum(1 if i>0 else -1 if i<0 else 0 for i in set(lst)) > 0

