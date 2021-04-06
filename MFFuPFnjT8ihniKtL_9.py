
def bug_jump(height, time):
    at = height**0.5
    if time <= 0 or time > at * 2000: return [0, None]
    ht = -(time/1000 - at)**2 + height
    return [round(ht,2), 'up' if time < at * 1000 else 'down']

