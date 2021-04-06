
def count_missing_nums(lst):
  lst = [int(i) for i in lst if i.isdigit()]
  mn,mx = min(lst),max(lst)
  a = 0
  for i in range(mn,mx):
    if i not in lst:
      a += 1
  return a

