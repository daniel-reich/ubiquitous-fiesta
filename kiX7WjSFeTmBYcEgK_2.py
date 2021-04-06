
def major_sum(lst):
  neg = abs(sum([i for i in lst if i < 0]))
  pos = sum([i for i in lst if i > 0])
  zero = lst.count(0)
  the_max = max(neg, pos, zero)
  if the_max == neg:
    return neg * -1
  return the_max

