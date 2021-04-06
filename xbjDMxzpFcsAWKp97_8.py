
def can_see_stage(seats):
  if len(seats)<=1:
    return True
​
  if all([i > j for i, j in zip(seats[-1], seats[-2])]):
    return can_see_stage(seats[:-1])
  else:
    return False

