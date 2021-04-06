
def is_prob_matrix(lst):
  print(lst)
  if verify_if_square(lst):
    if entries_are_in_range(lst):
      if rows_add_to_one(lst):
        return True
      else:
        return False
    else:
      return False
  else:
    return False
  
def rows_add_to_one(lst):
  for eachrow in lst:
    if sum(eachrow) == 1.0:
      continue
    else:
      return False
  return True
  
def entries_are_in_range(lst):
  for eachlist in lst:
    for eachnumber in eachlist:
      if eachnumber >= 0.0 and eachnumber <= 1.0:
        continue
      else:
        return False
  return True
  
def verify_if_square(lst):
  x = len(lst)
  for eachlist in lst:
    y = len(eachlist)
  if y != x:
    return False
  else:
    return True

