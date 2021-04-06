
def minutes_to_seconds(time):
    minutes = int(time.split(":")[0])
    seconds = int(time.split(":")[1])
​
    min_to_sec = minutes*60
​
    if seconds >= 60:
        return False
    else:
        return min_to_sec+seconds

