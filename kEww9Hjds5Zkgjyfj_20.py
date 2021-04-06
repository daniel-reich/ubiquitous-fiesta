
def replace_next_largest(l):
  a = sorted(l)
  return [-1 if l[i]==a[-1] else a[a.index(l[i])+1] for i in range(len(l))]

