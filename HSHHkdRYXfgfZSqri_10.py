
def damage(damage,speed,time):
  if damage < 0 or speed < 0:
    result = "invalid"
  else:
    if time == "second":
      result = damage * speed
    elif time == "minute":
      result = damage * speed * 60
    elif time == "hour":
      result = damage * speed * 3600
  return result

