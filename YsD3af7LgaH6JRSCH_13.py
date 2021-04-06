
def time_adjust(now, hrs, mins, sec):
    hours,minutes,seconds = now.split(':')
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    seconds += sec
    minutes_carry = seconds // 60
    seconds = seconds % 60
    minutes = minutes + minutes_carry + mins
    hours_carry = minutes // 60
    minutes = minutes % 60
    hours = hours + hrs + hours_carry
    hours = hours % 24
    return '{:0>2d}:{:0>2d}:{:0>2d}'.format(hours,minutes,seconds)

