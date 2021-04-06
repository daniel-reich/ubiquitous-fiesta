
def car_timer(n):
  hours = int(n / 60)
  minutes = n - hours * 60
  res = 0
  for ch in str(hours):
    res += int(ch)
  for ch in str(minutes):
    res += int(ch)
  return res

