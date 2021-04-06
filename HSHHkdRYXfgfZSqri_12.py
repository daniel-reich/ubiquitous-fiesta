
def damage(damage, speed, time):
  toseconds = {'second':1,'minute':60,'hour':3600}
  if damage < 0 or speed < 0: return "invalid"
  else: return damage * speed * toseconds[time]

