
def damage(damage, speed, time):
  if damage<0 or speed <0:
    return 'invalid'
  if time=='second':
    return damage*speed
  elif time=='minute':
    return damage*speed*60
  else:
    return damage*speed*3600

