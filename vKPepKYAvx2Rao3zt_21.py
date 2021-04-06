
def car_timer(n):
  sum = 0
  hor = n // 60
  min = n % 60
  hormin = str(hor) + str(min)
  for char in hormin:
    sum += int(char)
  return sum

