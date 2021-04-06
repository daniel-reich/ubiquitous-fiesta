
def quad_sequence(lst):
  #find pattern
  difference = [lst[len(lst)-2] - lst[len(lst)-3], lst[len(lst)-1] - lst[len(lst)-2]]
  difference_of_difference = difference[1] - difference[0]
  #workout
  last_num = lst[len(lst)-1]
  last_diff = difference[1]
  next_nums = []
  for _ in range(len(lst)):
    last_diff+=difference_of_difference
    last_num +=last_diff
    next_nums.append(last_num)
  return next_nums

