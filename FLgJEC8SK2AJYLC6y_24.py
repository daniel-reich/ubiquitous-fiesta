
def possible_path(lst):
  paths = {'H':(2, 4), 1:(2,), 2:(1,'H'), 3:(4,), 4:(3,'H')}
  for i, p in enumerate(lst[1:]):
    if p not in paths.get(lst[i]):
      return False
  return True

