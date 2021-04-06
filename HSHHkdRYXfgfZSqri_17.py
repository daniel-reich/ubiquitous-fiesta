
def damage(damage, speed, time):
  if damage < 0 or speed < 0:
    return "invalid"
  else: 
    mult = 0
    if time == "second": 
      mult = 1
    elif time == "minute":
      mult = 60
    elif time == "hour": 
      mult = 60*60
    return damage*speed*mult

