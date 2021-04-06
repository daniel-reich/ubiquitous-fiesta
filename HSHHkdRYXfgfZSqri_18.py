
factors = {"second": 1, "minute": 60, "hour": 3600}
​
def damage(damage, speed, time):
    return "invalid" if min(damage, speed) < 0 else damage * speed * factors[time]

