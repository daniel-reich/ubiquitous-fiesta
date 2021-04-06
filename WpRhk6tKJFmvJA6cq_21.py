
def manage_delays(train, dest, delay):
    if dest in t.destinations:
        h, m = t.expected_time.split(':')
        min = int(h) * 60 + int(m) + delay
        new_min = str(min%60).zfill(2)
        new_hrs = str((min//60) % 24).zfill(2)
        t.expected_time = new_hrs + ':' + new_min

