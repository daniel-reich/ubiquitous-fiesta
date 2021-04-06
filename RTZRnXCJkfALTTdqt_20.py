
def sum_neg(lst):
  if not lst:
    return lst
  else:
    count_even = 0
    sum_odd = 0
    for i in lst:
      if i < 0:
        sum_odd += i
      else:
        count_even += 1
    return [count_even, sum_odd]

