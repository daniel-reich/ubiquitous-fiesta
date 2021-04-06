
def break_point(num):
  from itertools import accumulate
  accum = list(accumulate([int(x) for x in str(num)]))
  return sum(x for x in accum if x == max(accum)/2) > 1

