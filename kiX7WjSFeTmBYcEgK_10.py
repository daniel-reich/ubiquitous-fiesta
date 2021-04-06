
def major_sum(x):
  p = sum([i for i in x if i > 0])
  n = sum([i for i in x if i < 0])
  return n if -n > p else x.count(0) if x.count(0) > len(x) // 2 else p

