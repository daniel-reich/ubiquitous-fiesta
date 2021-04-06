
def polygon(lst):
  lst = [[e[0]-lst[0][0],e[1]-lst[0][1]] for e in lst]
  lst = sorted(lst[1:], key = lambda e: sum(e[0]*f[1]-e[1]*f[0]>0 for f in lst))
  lst = [[0,0]]+lst+[[0,0]]
  return abs(sum((lst[i][1]*lst[i-1][0]-lst[i][0]*lst[i-1][1])/2 for i in range(1,len(lst))))

