
def lets_meet(distance, va, vb):
    c = (va + vb)
    x = distance / c
    seconds = x * 60 * 60
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    #a="%2dh%02dmin%2ds" % (hours, minutes, seconds)
    result = ('{}h {}min {}s'.format(int(hours), int(minutes),int(seconds)))
​
    return result

