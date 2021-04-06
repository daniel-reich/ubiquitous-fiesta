
def antipodes_average(lst):
  x = [lst[:len(lst)//2], lst[len(lst)//2:]]
  return [(x[0][i] + x[1][-(i+1)])/2 for i in range(len(x[0]))]

