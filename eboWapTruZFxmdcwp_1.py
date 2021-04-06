
def is_positive_dominant(lst):
  lst = set(lst)
  pos = sum(i>0 for i in lst)
  neg = sum(i<0 for i in lst)
  return pos>neg

