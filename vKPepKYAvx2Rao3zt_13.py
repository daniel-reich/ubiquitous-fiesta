
def car_timer(n):
  hours, mins = divmod(n, 60)
  return sum(int(i) for i in str(hours) + str(mins))

