
def longest_time(h, m, s):
  a,b = [h,m,s],[h*3600,m*60,s]
  return a[b.index(max(b))]

