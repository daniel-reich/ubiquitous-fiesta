
def index_multiplier(lst):
  for i in range(0, len(lst)):
    lst[i] *= i
  return sum(lst)

