
def deep_count(lst):
  counta=0
  for i in lst:
    if (isinstance(i,list)):
      counta+=deep_count(i)
  return len(lst)+counta

