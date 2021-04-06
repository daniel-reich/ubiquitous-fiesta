
def power_ranger(power, minimum, maximum):
    start = round(minimum**(1/power))
    stop = round(maximum**(1/power)) + 1
    return len([x**power for x in range(start, stop)])

