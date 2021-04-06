
def microwave_buttons(time):
    min, sec = map(str, time.split(":"))
    tots = int(min) * 60 + int(sec)
    if 0 < tots <= 99:
        if tots == 30:
            return 2
        else:
            return 3
    elif tots == 0:
        return 1
    else:
        return len(str(int(min)) + sec) + 1

