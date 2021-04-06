
def car_timer(n):
  time = list(map(str,divmod(n,60)))
  return sum(int(j) for i in time for j in i)

