
def car_timer(n):
  h = str(n // 60) if n > 60 else '00'
  m = str(n % 60) if n > 60 else str(n)
  return sum(map(int, h)) + sum(map(int, m))

