
def car_timer(n):
  h,m=divmod(n,60)
  H=str(h).zfill(2)
  M=str(m).zfill(2)
  return sum(int(x) for x in H)+sum(int(y) for y in M)

