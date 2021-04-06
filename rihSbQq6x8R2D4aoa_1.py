
def alpha_range(start, stop, step=1):
    t, p = ord(start), ord(stop)
    if step == 0 or 26 < step or step < -26:
        return "step must be a non-zero value between -26 and 26, exclusive"
    elif (start.islower() != stop.islower()) or (start.isupper() != stop.isupper()):
        return "both start and stop must share the same case"
    elif step < 0:
        return list(map(chr, range(max(t, p), min(t, p) - 1, step)))
    else:
        return list(map(chr, range(min(t, p), max(t, p) + 1, step)))

