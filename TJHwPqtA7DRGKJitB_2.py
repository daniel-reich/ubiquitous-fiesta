
def is_prob_matrix(lst):
  for row in lst:
    if len(row) != len(lst):
      return False
    
    if sum(row) != 1:
      return False
      
    for i in row:
      if i < 0 or i > 1:
        return False
  return True

