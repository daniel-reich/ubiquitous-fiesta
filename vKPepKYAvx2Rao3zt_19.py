
def car_timer(n):
  h,m=divmod(n,60)
  sum_h=sum([int(x) for x in str(h)])
  sum_m=sum([int(x) for x in str(m)])
  return sum_h+sum_m

