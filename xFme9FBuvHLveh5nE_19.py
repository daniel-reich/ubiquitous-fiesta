
def is_zygodrome(num):
  if num < 10: return False
  car, *cdr  = str(num)
  for i in cdr:
    if i in car:
      car += i
    else:
      if len(car) < 2:
        return False
      else:
        car = i
  return True if len(car) > 1 else False

