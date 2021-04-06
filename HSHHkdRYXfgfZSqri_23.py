
def damage(damage, speed, time):
  if speed<0 or damage<0:
    return "invalid"
  elif time =="second":
    return damage*speed
  elif time == "minute":
    return (damage*speed)*60
  elif time == "hour":
    return (damage*speed)*3600

