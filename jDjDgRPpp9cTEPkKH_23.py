
def over_time(details):
    '''
    Returns pay due based on details: start time, end time, hourly rate
    and overtime rate. Normal pay for hours worked between 9am and 5pm.
    '''
    start, end, rate, otime = details
    hrs_worked = end - start   # assume all on single day!
    normal_hrs = max(0, min(end, 17) - max(start, 9))  # assume don't start before 9!
    
    result = rate * (normal_hrs + (hrs_worked - normal_hrs) * otime) + 0.001
    return '${:.2f}'.format(result)

