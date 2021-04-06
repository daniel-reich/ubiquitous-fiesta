
def is_positive_dominant(lst):
  lst = set(lst)
  lst = [i for i in lst if i != 0]
  return sum(1 if i > 0 and i != 0 else -1 for i in lst) > 0

