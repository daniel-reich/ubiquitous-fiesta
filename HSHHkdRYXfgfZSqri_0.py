
def damage(damage, speed, time):
  secs = {'second':1, 'minute':60, 'hour':3600}
  ans = damage*speed*secs[time]
  return ans if ans>0 and speed>0 else 'invalid'

