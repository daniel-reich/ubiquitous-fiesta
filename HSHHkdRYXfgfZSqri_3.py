
def damage(damage, speed, time):
  if damage < 0 or speed < 0: return "invalid"
  times = {"hour": 3600, "minute": 60, "second": 1}
  return damage * speed * times[time]

