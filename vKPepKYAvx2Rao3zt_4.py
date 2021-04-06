
def car_timer(n):
  return sum(int(i) for i in str(divmod(n, 60)) if i.isdigit())

