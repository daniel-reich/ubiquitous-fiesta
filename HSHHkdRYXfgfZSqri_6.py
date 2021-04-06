
def damage(dam, speed, time):
    if dam< 0 or speed < 0:
        return "invalid"
    timedict = {"second":1, "minute":60, "hour":3600}
    return(speed*(timedict[time])*dam)

