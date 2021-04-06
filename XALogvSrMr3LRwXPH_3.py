
def is_shuffled_well(lst):
  for i in range(len(lst)-3):
    a = [lst[i], lst[i]+1, lst[i]+2]
    b = [lst[i], lst[i]-1, lst[i]-2]
    y = lst[i:i+3]
    if a == y or b == y:
      return False
  return True

