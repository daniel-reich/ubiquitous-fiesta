
def balanced(lst):
  mid = len(lst) // 2
  lo = lst[:mid]
  hi = lst[mid:]
  return (hi, lo)[sum(lo) >= sum(hi)] + (lo, hi)[sum(lo) <= sum(hi)]

