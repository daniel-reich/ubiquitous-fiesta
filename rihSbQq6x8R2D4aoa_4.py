
def alpha_range(start, stop, step=1):
    if step < -26 or step > 26 or step == 0:
        return "step must be a non-zero value between -26 and 26, exclusive"
    elif ((start.isupper() and stop.islower()) or
          (start.islower() and stop.isupper())):
        return "both start and stop must share the same case"
    b, e = ord(start), ord(stop)
    if (e < b and step > 0) or (step < 0 and b < e):
        b, e = e, b
    return [chr(i) for i in range(b, e + (1 if step > 0 else -1), step)]

