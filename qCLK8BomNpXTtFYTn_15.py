
def cumulative_sum(lst):
  return [sum(lst[:ind]) + i for ind, i in enumerate(lst)]

