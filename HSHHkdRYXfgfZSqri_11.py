
def damage(damage, speed, time):
    if(damage<0 or speed<0): return 'invalid'
    s = damage * speed
    if(time == 'second'): return s
    if(time == 'minute'): return (s*60)
    if(time == 'hour'): return (s*60*60)

