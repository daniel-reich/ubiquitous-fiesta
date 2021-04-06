
def grab_number_sum(s):
    sum_nums = 0
    begin = -1
    for i, c in enumerate(s):
        if c.isdigit() and begin < 0:
            begin = i
        elif not c.isdigit() and begin >= 0:
            sum_nums += int(s[begin: i])
            begin = -1
        elif c.isdigit() and i == len(s) - 1:
            sum_nums += int(s[begin: i + 1])
    return sum_nums

