
def weekly_salary(hours):
    r = 0
    for y, x in enumerate(hours):
        if x <= 8:
            add = 10 * x
        else:
            add = 80 + (x - 8) * 15 
        if y > 4:
            add = add * 2
        r += add
    return r

