
def is_equal(lst):
  return sum([int(i) for i in list(str(lst[0]))]) == sum([int(i) for i in list(str(lst[1]))])

