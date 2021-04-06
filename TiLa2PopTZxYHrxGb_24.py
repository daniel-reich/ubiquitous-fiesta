
def playback_duration(duration, speed):
    h,m,s=duration.split(':')
    totSec=(3600*int(h)+60*int(m)+int(s))/speed
    h=totSec//3600
    totSec=totSec%3600
    m=totSec//60
    s=totSec%60
    return str('{:02d}:{:02d}:{:02d}'.format(int(h),int(m),int(s)))

