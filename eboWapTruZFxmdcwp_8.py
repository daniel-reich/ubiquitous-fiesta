
def is_positive_dominant(lst):
  return len(set([i for i in lst if i > 0])) > len(set([i for i in lst if i < 0]))

