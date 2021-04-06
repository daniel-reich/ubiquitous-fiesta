
import re
def swap_xy(txt):
    lst = [int(d) for d in re.findall(r'-?\d+', txt)]
    for i in range(0, 3, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return '(%d, %d), (%d, %d)' % (lst[0], lst[1], lst[2], lst[3])

