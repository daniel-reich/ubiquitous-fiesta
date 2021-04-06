
def possible_path(lst):
  if len(lst)==1:
    return True
  l=[type(x) for x in lst]
  return all(x!=l[i+1] for i,x in enumerate(l[:-1]))

