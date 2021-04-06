
def time_to_eat(current_time):
    
    time = current_time.split()
    hours = time[0].split(':')[0]
    minutes = time[0].split(':')[1]
    
    ret = [0,0]
    
    if hours == '12' or hours == '11':
        if minutes == '00':
            ret[0] = abs(ret[0] - 7)
        else:
            ret[0] = abs(ret[0] - 6)
            ret[1] += (60 - int(minutes))
        
    if int(hours) < 7:
        if minutes == '00':
            ret[0] += (7 - int(hours))
        else:
            ret[0] += (6 - int(hours))
            ret[1] += (60 - int(minutes))
​
    if time[-1] == 'a.m.' and 7 <= int(hours) <= 10:
        if minutes == '00':
            ret[0] += (12 - int(hours))
        else: 
            ret[0] += (11 - int(hours))
            ret[1] += (60 - int(minutes))
    
    if hours == '11':
        ret[0] += 1
        
    return ret

