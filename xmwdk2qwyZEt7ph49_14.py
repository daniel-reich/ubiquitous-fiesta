
def get_length(lst):
  r=0
  for i in lst:
    if type(i) is list: r+=get_length(i)
    else: r+=1
  return r

