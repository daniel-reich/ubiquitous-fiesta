
def is_positive_dominant(lst):
  return len([i for i in set(lst) if i>0]) > len([i for i in set(lst) if i<0])

