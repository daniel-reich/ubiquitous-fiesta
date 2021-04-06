
def antipodes_average(lst):
  return [0.5 * (lst[i] + lst[-(i+1)]) for i in range(len(lst)//2)]

