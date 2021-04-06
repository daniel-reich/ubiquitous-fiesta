
def time_adjust(now, hrs, mins, sec):
    h, m, s = now.split(':')
    h = (int(h)+hrs+(int(m)+mins+(int(s)+sec)//60)//60)%24
    m = (int(m)+mins+(int(s)+sec)//60)%60
    s = (int(s)+sec)%60
    if(h<10): h = '0' + str(h)
    if(m<10): m = '0' + str(m)
    if(s<10): s = '0' + str(s)
    return  str(h) + ':' + str(m) + ':' + str(s)

