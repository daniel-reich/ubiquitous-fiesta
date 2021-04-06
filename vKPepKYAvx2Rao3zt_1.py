
def car_timer(n):
  h = n // 60
  m = n - h * 60 
  return sum(int(x) for x in str(h % 24) + str(m))

