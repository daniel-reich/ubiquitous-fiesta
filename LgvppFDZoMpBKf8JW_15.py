
def digital_clock(seconds):
    hours = int((seconds / 3600) // 1)
    minutes = int((seconds / 60 - hours * 60) // 1)
    seconds = int(seconds - hours * 3600 - minutes * 60)
    if hours < 10:
        hours = "0" + str(hours)
    if hours == 24:
        hours = "00"
    if minutes < 10:
        minutes = "0" + str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)
    return str(hours) + ":" + str(minutes) + ":" + str(seconds)

