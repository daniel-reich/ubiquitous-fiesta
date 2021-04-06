
def damage(damage, speed, time):
  if damage < 0 or speed < 0:
    return 'invalid'
  else:
    if time == 'second':
      return damage * speed
    if time == 'minute':
      return damage * speed * 60
    if time == 'hour':
      return damage * speed * 3600

