
def damage(damage, speed, time):
  if(damage < 0 or speed < 0):
    return "invalid"
  second = 1
  if(time == "minute"):
    second = 60
  if(time == "hour"):
    second = 60*60
  return second * damage * speed

