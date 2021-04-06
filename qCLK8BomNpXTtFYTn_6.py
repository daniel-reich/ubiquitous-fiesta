
def cumulative_sum(lst):
  return [num + sum(lst[:x]) for x,num in enumerate(lst)]

