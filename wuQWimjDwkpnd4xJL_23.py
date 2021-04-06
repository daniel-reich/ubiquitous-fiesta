
def balanced(lst):
  first_half = lst[:len(lst)//2]
  second_half = lst[len(lst)//2:]
  
  if sum(first_half) > sum(second_half):
    return first_half + first_half 
  elif sum(first_half) < sum(second_half):
    return second_half + second_half
  else:
    return lst

