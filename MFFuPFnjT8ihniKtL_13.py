
def bug_jump(height, time):
    half_time, t = pow(height, 0.5), time / 1000
    if t > 2 * half_time:
        return [0, None]
    return [round(height - pow(t - half_time, 2), 2),
            'up' if t < half_time else 'down']

