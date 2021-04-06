
def longest_time(h, m, s):
  orig = [h,m,s]
  temp = [h*60*60,m*60,s]
  return orig[temp.index(max(temp))]

