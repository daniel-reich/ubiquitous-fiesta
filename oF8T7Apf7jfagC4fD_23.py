
def antipodes_average(lst):
  first, second = lst[:len(lst)//2], lst[len(lst) - len(lst)//2:]
  return [(a+b)/2 for a, b in zip(first, second[::-1])]

