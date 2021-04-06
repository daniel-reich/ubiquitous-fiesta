
def time_sum(times):
  h,m,s=map(sum, zip(*(map(int, t.split(':')) for t in ['0:0:0']+times)))
  return [h+(m+s//60)//60,(m+s//60)%60,s%60]

