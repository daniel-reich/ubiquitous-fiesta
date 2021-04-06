
def alpha_range(start, stop, step=1):
    if step == 0 or abs(step) > 26:
        return "step must be a non-zero value between -26 and 26, exclusive"
    if (start <= 'Z' and stop > 'Z') or (start >= 'a' and stop < 'a'):
        return "both start and stop must share the same case"
    start, stop = ord(start), ord(stop)
    if step > 0:
        start, stop = min(start, stop), max(start, stop)
    else:
        start, stop = max(start, stop), min(start, stop)
    return [chr(k) for k in range(start, stop+(step//abs(step)), step)]

