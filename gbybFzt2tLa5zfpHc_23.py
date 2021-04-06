
def three_sum(lst):
  def get_sublists(lst):
    from itertools import combinations as c
    sublists = list(c(lst,3))
    return sublists
  def sum_to_zero(lst):
    return sum(lst) == 0
​
  sublists = get_sublists(lst)
  equal_zero = []
 
  for sublist in sublists:
    if sum_to_zero(sublist) == True and list(sublist) not in equal_zero:
      equal_zero.append(list(sublist))
  
  return equal_zero
  return equal_zero

