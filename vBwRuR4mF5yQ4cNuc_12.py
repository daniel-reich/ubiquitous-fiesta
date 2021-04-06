
def count_missing_nums(lst):
  n = [int(i) for i in lst if i.isnumeric()]
  mn, mx = min(n), max(n)
  m = [j for j in range(mn,mx+1)]
  return len(m) - len(n)

