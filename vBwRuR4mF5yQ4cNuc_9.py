
def count_missing_nums(lst):
  l=sorted(map(int,[x for x in lst if x.isdigit()]))
  return sum(1 for i in range(l[0],l[-1]) if i not in l)

