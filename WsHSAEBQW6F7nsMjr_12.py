
def flatten_the_curve(lst):
  if(lst == []):
    return []
  else:
    x = round(sum(lst)/len(lst), 1);
    return [x for i in lst]

