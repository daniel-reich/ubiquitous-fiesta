
def is_checkerboard(lst):
  z = [a[i]==b[i] for a,b in zip(lst, lst[1:]) for i in range(len(a))]
  l = [a==b for i in lst for a,b in zip(i, i[1:])]
  return not (any(z) or any(l))

