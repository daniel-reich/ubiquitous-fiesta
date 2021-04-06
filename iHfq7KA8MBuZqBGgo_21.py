
def is_legitimate(lst):
  return not(any([1 for x in lst[0] if x==1]) or any([1 for x in lst[-1] if x==1]) or any([1 for x in lst if x[0]==1]) or any([1 for x in lst if x[-1]==1]))

