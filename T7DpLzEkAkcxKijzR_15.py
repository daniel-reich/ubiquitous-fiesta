
def cars_needed(n):
  if n == 0:
    return 0
  elif n <= 5:
    return 1
  elif n > 5:
    car = n // 5
    if n%5 == 0:
      return car
    elif n%5 != 0 :
      return car + 1
  else:
    return "Whoops!"

