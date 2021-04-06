
def is_slidey(n):
  l = [int(i) for i in str(n)]
  return set([abs(l[i] - l[i+1]) for i in range(len(l)-1)])=={1} or len(str(n))==1

