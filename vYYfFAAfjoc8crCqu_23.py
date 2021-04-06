
def tree(h):
  space = lambda h, n: " " * (((h*2)-1-n)//2)
  trees = [space(h, n) + ("#" * n) + space(h,n) for n in range(1, h*2, 2)]
  return trees

