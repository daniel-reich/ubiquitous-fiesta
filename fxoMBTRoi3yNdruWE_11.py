
def in_box(lst):
  box_dim = len(lst[0])
  for i in range(1, box_dim - 1):
    if '*' in lst[i][1:-1]:
      return True 
  return False

