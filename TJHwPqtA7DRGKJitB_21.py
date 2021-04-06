
def is_prob_matrix(lst):
  if len(lst) != len(lst[0]):
    return False
  for x in lst:
    for y in x:
      if y < 0 or y > 1:
        return False
    if int(sum(x)) != 1:
      return False
  return True

