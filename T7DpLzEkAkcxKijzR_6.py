
def cars_needed(n):
  cars, extra = divmod(n, 5)
  return cars + 1 if extra else cars

