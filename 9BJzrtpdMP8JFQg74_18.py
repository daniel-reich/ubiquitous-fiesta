
def twins(lst):
  return [i for i in range(len(lst)) if sum(lst[:i]) == sum(lst)/2][0]

