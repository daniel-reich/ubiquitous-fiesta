
def cumulative_sum(lst):
  return [sum(lst[:i+1]) for i, v in enumerate(lst)]

