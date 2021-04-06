
def time_to_eat(current_time):
    #changing the string to a list
    current_time = current_time.replace(' ', ':')
    current_time = current_time.split(':')
​
    #changing hours and minutes to integers
    current_time[0] = int(current_time[0])
    current_time[1] = int(current_time[1])
​
    #7AM and 7PM are both meal times
    if current_time[0] == 7 and current_time[1] == 0:
        hours = 0
        minutes = 0
        return [hours, minutes]
​
    #different conditions for AM
    elif 'a.m.' in current_time:
        if current_time[0] < 7:
            hours = 7 - current_time[0]
            if current_time[1] == 0:
                minutes = 0
                return [hours, minutes]
            else:
                hours -= 1
                minutes = 60 - current_time[1]
                return [hours, minutes]
​
        elif current_time[0] == 12:
            hours = 7
            minutes = 0
            return [hours, minutes]
        else:
            hours = 12 - current_time[0]
            if current_time[1] == 0:
                minutes = 0
                return [hours, minutes]
            else:
                hours -= 1
                minutes = 60 - current_time[1]
                return [hours, minutes]
​
​
    if 'p.m.' in current_time:
        if current_time[0] == 12 and current_time[1] == 0:
            hours = 0
            minutes = 0
            return [hours, minutes]
        elif current_time[0] < 7:
            hours = 7 - current_time[0]
            if current_time[1] == 0:
                minutes = 0
                return [hours, minutes]
            else:
                hours -= 1
                minutes = 60 - current_time[1]
                return [hours, minutes]
        else:
            hours = 7 + (12 - current_time[0])
            if current_time[1] == 0:
                 minutes = 0
                 return [hours, minutes]
            else:
                hours -= 1
                minutes = 60 - current_time[1]
                return [hours, minutes]

