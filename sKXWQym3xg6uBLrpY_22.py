
def iqr(lst):
  n = len(lst)
  s_lst = sorted(lst)
  if n % 2 == 1:
    del s_lst[int(n//2)]
    n -= 1
    
  m = n//2
  if m % 2 == 0:
    Q1 = s_lst[m//2-1]/2 + s_lst[m//2]/2
    Q3 = s_lst[m+m//2-1]/2 + s_lst[m+m//2]/2
  else:
    Q1 = s_lst[m//2]
    Q3 = s_lst[m+m//2]
    
  return Q3 - Q1

