
def damage(damage, speed, time):
  if damage >= 0 and speed >= 0:
    if time == "second":
      return damage * speed
    elif time == "minute":
      return damage * (speed * 60)
    elif time == "hour":
      return damage * (speed * 60 * 60)
  
  else:
    return "invalid"

