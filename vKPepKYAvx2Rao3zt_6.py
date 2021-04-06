
def car_timer(n):
  return sum([int(i) for i in str(n//60)])+sum([int(i) for i in str(n%60)]) if n > 60 else sum([int(i) for i in str(n)]) if n > 20 else n

