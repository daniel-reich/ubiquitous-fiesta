
def antipodes_average(lst):
  x = len(lst)//2
  first, second = lst[:x], lst[x:][::-1]
  return [(i+j)/2 for i,j in zip(first, second)]

