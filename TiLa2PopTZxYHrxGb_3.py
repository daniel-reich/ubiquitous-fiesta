
def playback_duration(duration, speed):
    '''
    Returns the duration adjusted for speed as per instructions
    '''
    h,m,s = (int(t) for t in duration.split(':'))
    d2 = int((h*3600 + m*60 + s)/speed)
    h2 = d2 // 3600
    m2 = (d2 - h2*3600) // 60
    s2 = d2 - h2*3600 - m2*60
​
    return '{:02d}:{:02d}:{:02d}'.format(h2,m2,s2)

