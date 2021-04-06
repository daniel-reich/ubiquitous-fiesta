
def solve(item):
    wake, duration = item
    h, m = [int(_) for _ in wake.split(':')]
    duration_h, duration_m = [int(_) for _ in duration.split(':')]
    h = (h - duration_h) % 24
    for _ in range(duration_m):
        m -= 1
        if m == -1:
            m = 59
            h -= 1
    h %= 24
    return str(h).zfill(2) + ':' + str(m).zfill(2)
        
    
def bed_time(*args):
    return [solve(item) for item in args]

