
def sum_of_evens(lst):
  val = 0
  for thing in lst:
    for num in thing:
      if num % 2 == 0:
        val += num
  return val

