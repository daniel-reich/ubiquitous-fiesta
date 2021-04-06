
def time_to_eat(current_time):
    breakfast = 7
    lunch = 12 
    dinner = 19
    actuall_time = current_time.split(" ")
    times = actuall_time[0].split(":")
​
    hours = int(times[0])
    minutes = int(times[1])
​
    intervall = actuall_time[1]
​
    time_left = []
​
    if intervall == "p.m.":
        hours += 12
​
    #time until dinner
    if hours <= dinner and hours >= lunch:
        hours = dinner - hours
        if minutes != 0:
            time_left.append(hours-1)
            time_left.append(60-minutes)
        else:
            time_left.append(hours)
            time_left.append(minutes)
​
    #time until lunch
    elif hours <= lunch and hours >= breakfast:
        hours = lunch - hours
        if minutes != 0:
            time_left.append(hours-1)
            time_left.append(60-minutes)
        else:
            time_left.append(hours)
            time_left.append(minutes)
​
    #time until breakfast
    elif hours > dinner:
        hours = abs(24 - hours) + breakfast
        if minutes != 0:
            time_left.append(hours-1)
            time_left.append(60-minutes)
        else:
            time_left.append(hours)
            time_left.append(minutes)
    elif hours < breakfast:
        hours = breakfast - hours
        if minutes != 0:
            time_left.append(hours-1)
            time_left.append(60-minutes)
        else:
            time_left.append(hours)
            time_left.append(minutes)
​
    return time_left

