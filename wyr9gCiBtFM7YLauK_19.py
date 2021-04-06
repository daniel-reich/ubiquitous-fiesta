
def time_sum(times):
  s = 0
  for t in times:
    h1,m1,s1 = map(int,t.split(':'))
    s += h1*3600 + m1*60 + s1
  h,r = divmod(s,3600)
  m,s = divmod(r,60)
  return [h,m,s]

