
def cumulative_sum(lst):
  return [sum(lst[:n+1]) for n in range(len(lst))]

