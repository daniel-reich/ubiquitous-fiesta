
def microwave_buttons(time):
    t = time.split(':')
    m,n = map(int,t)
    press = 0
    if n == 0 and m == 0:
        return 1
    elif m == 0:
        if n < 9:
            press+=1
        elif n == 30:
            press += 1
        else:
            press+=2
    else:
        if m > 9:
            press+=4
        else:
            press+=2
    return press + 1

