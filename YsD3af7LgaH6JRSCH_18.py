
def time_adjust(now, hrs, mins, sec):
    seconds = int(now[6:]) + sec
    minutes = int(now[3:5]) + mins + seconds //60  
    hours = int(now[:2]) + hrs + minutes // 60
    return '{:02d}:{:02d}:{:02d}'.format(hours % 24,minutes % 60,seconds % 60)

