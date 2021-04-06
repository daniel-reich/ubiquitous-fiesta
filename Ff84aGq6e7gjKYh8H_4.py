
def minutes_to_seconds(time):
    return int(time.split(':')[0])*60 + int(time.split(':')[1]) if int(time.split(':')[1]) < 60 else False

