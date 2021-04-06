
def sum_of_evens(lst):
  reglst = []
  for i in lst:
    for item in i:
      reglst.append(item)
  return sum([x for x in reglst if x % 2 == 0])

