
def damage(damage, speed, time):
  n = damage*speed
  return "invalid" if min(damage,speed)<0 else n*60 if time=="minute" else n*3600 if time == "hour" else n

