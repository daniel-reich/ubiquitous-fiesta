
def hours_passed(time1, time2):
    time1 = eval(time1.replace(' AM','').replace(' PM','+12').replace(':00',''))
    time2 = eval(time2.replace(' AM','').replace(' PM','+12').replace(':00',''))
    if time1==12:time1=0
    return str(abs(time2-time1)) + ' hours' if time1!=time2 else 'no time passed'

