
def count_boomerangs(lst):
  result = 0
  for i in range(0,len(lst) - 2): 
    if (lst[i] == lst[i+2] and lst[i] != lst[i+1]): result += 1 
  return result

