
def car_timer(n):
  x = str(n//60) + str(n%60)
  return sum(int(i) for i in x)

