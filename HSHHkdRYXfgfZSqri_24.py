
def damage(damage, speed, time):
  if time == "second":
    seconds = speed
  elif time == "minute":
    seconds = speed * 60
  elif time == "hour":
    seconds = speed *60 *60
  if damage < 0 or speed < 0:
    return "invalid"
  final = damage *seconds
  return final

