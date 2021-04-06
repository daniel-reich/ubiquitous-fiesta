
def damage(damage,speed,time):
    result = damage * speed
    if damage > 0 and speed > 0:
        if time == "second":
            result1 = result*1
            return result1
        elif time == 'minute':
            result1 = result * 60
            return result1
        elif time == 'hour':
            result1 = result * 3600
            return result1
    else:
        return "invalid"

