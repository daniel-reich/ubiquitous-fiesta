
import datetime
def time_to_eat(current_time):
    col_index = current_time.index(':')
    h = int(current_time[:col_index])
    if current_time[col_index+4] == 'p':
        h += 12
    m = int(current_time[col_index+1:col_index+3])
    ct = datetime.time(h,m)
    ctm = h*60+m
    t1 = datetime.time(7)
    t1m = 7*60
    t2 = datetime.time(12)
    t2m = 12*60
    t3 = datetime.time(19)
    t3m = 19*60
    #meals = [t1,t2,t3]
    if ctm < t1m:
        return [int((t1m-ctm)/60),(t1m-ctm)%60]
    if ctm < t2m:
        return [int((t2m-ctm)/60),(t2m-ctm)%60]
    if ctm < t3m:
        return [int((t3m-ctm)/60),(t3m-ctm)%60]
    else:
        return [int((t1m+24*60-ctm)/60),(t1m+24*60-ctm)%60]

