
def sum_two_smallest_nums(lst):
  lst.sort()
  for i in range(len(lst)):
    if (lst[i] >=0):
      return lst[i]+lst[i+1]

