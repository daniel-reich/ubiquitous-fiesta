
def damage(damage, speed, time):
  seconds = {'second': 1, 'minute': 60, 'hour': 3600}
  if (damage >=0) and (speed >= 0):
    return damage * speed * seconds[time]
  else:
    return "invalid"

