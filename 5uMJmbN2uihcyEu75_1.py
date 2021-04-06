
def weekly_salary(hours):
    hours += hours[-2:]
    total = 0
    for i in hours:
        if i <= 8:
            total += i*10
        else:
            total += 80 + (i-8)*15
    return total

