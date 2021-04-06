
def damage(damage, speed, time):
  seconds = {'hour' : 3600 , 'minute' : 60 , 'second': 1}
  dmg =  damage * speed * seconds[time]
  if damage < 0 or speed < 0:
    return 'invalid'
  else:
    return dmg

