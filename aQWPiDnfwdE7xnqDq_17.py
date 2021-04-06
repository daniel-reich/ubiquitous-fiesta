
def drange(*args):
    significance_start, significance_step = 0, 0
    if len(args) == 3:
        str_start = str(args[0])
        if '.' in str_start:
            significance_start = len(str_start) - 1 - str_start.index('.')
        str_step = str(args[2])
        if '.' in str_step:
            significance_step = len(str_step) - 1 - str_step.index('.')
    significance = max(significance_start, significance_step)
    res = []
    x, end, step = 0, args[0], 1
    if len(args) > 1:
        x = args[0]
        end = args[1]
    if len(args) > 2:
        step = args[2]
    while x < end:
        res.append(round(x, significance))
        x += step
    return tuple(res)

