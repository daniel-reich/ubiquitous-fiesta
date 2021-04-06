
def check(lst):
  sorted_lst = sorted(lst)
  m = min(lst)
  if lst.index(m) == 0: return 'NO'
  rotated_lst = lst[lst.index(m):] + lst[0:lst.index(m)]
  if rotated_lst == sorted_lst: return 'YES'
  else: return 'NO'

