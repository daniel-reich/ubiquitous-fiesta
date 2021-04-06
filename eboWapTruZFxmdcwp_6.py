
def is_positive_dominant(lst):
  return len(set(filter(lambda x: x>0,lst)))>len(set(filter(lambda x: x<0,lst)))

