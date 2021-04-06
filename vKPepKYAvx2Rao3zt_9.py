
def car_timer(n):
  minutes = n%60
  hours = n // 60
  return (minutes%10) + (hours % 10) + minutes//10 + hours // 10

