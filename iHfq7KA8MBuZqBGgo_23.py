
def is_legitimate(lst):
  return sum(i[0] + i[-1] for i in lst) + sum(lst[0]) + sum(lst[-1]) < 1

