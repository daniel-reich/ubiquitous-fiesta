
def weekly_salary(hours):
    week = hours[-2:]
    work = hours[:-2]
    overtime1 = sum([i-8 for i in work if i>=8])
    overtime2 = sum([i-8 for i in week if i>=8])
    a = ((sum(work)-overtime1)*10) + (overtime1*15)
    b = ((sum(week)-overtime2)*20) + (overtime2*30)
    return a+b

