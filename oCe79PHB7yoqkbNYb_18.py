
def break_point(num):
  a = [int(i) for i in str(num)]
  return any([sum(a[:i])==sum(a[i:]) for i in range(1,len(a))])

