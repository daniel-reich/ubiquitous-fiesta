
def leader(lst):
  a = lst[lst.index(max(lst)):]
  return [a[i-1] for i in range(len(a)) if a[i-1] > a[i]] + [a[-1]]

