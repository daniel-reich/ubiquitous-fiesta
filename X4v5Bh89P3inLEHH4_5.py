
def spin_around(lst):
    degrees = 0
    spincount = 0
    for x in lst:
        if x == 'right':
            degrees = degrees + 90
        elif x == 'left':
            degrees = degrees - 90
    spincount = abs(degrees) // 360
    spincount = abs(spincount)
    return spincount

