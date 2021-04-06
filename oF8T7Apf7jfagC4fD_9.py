
def antipodes_average(a):
  r, l = a[:len(a)//2], a[-1:-len(a)//2-1:-1]
  return [(r[i] + l[i]) / 2 for i in range(len(r))]

