
def all_pos(x):
  return [j for i in x for j in range(len(x)) if i == x[j]]
  
def check_pattern(lst, pattern):
  return all_pos(lst) == all_pos(pattern)

