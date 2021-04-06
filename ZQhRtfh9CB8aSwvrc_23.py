
def greater_than_sum(lst):
  return all([y > sum(lst[:x]) for (x,y) in enumerate(lst)])

