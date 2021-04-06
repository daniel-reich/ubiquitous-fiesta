
def translate(ran, num):
    ran2 = ran * ran
    mirror = ran2 - num
    if mirror < 0:
        return '{} is not in the range [0:{}]'.format(num, ran2)
    f_steps = mirror - num
    b_steps = 2 * min(mirror, num) + 1
    if abs(f_steps) == b_steps:
        return '+{0} or -{0} ---> {1}'.format(b_steps, mirror)
    steps = (f_steps if abs(f_steps) < b_steps
             else (-b_steps if f_steps > 0 else b_steps))
    return '{:+d} ---> {}'.format(steps, mirror)

