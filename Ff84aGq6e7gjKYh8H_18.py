
def minutes_to_seconds(time):
    l = time.split(":")
    return int(l[1])+int(l[0])*60 if int(l[1]) < 60 else False

