
def time_sum(times):
    times = [[int(n) for n in t.split(':')] for t in times]
    seconds = sum(t[2] for t in times)
    minutes = sum(t[1] for t in times) + seconds // 60
    hours = sum(t[0] for t in times) + minutes // 60
    return [hours, minutes%60, seconds%60]

