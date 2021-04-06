
def bed_time(*times):
​
    return_strs=[]
    for alarm,duration in times:
​
        alarm_hr= int(alarm[:2]) if alarm[0]!='0' else int(alarm[1:2])
        alarm_min=(60*alarm_hr)+ (int(alarm[3:]) if alarm[3]!='0' else int(alarm[4:]))
​
        duration_hr = int(duration[:2]) if duration[0] != '0' else int(duration[1:2])
        duration_min =(60*duration_hr)+ (int(duration[3:]) if duration[3] != '0' else int(duration[4:]))
        sleep_min=(alarm_min-duration_min)%(24*60)
​
        return_strs.append(str(sleep_min//60).zfill(2)+':'+str(sleep_min%60).zfill(2))
​
    return return_strs

