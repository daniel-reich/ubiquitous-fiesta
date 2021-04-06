
def damage(damage, speed, time):
  if time is "second":
    time = 1
  elif time is "minute":
    time = 60
  else:
    time = 3600
  if damage < 0 or speed < 0:
    return "invalid"
  else:
    return damage * speed * time

