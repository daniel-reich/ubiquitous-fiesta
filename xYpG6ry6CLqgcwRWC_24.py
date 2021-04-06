
def sum_two_smallest_nums(lst):
  lst.sort()
  lst1 = list(filter(lambda i: i > 0, lst))
  total = lst1[0] + lst1[1]
  return total

