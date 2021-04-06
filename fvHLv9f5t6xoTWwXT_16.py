
def grab_number_sum(s):
    n = ''
    tot = 0
    for x in s:
        if x.isdigit():
            n += x
        else:
            if n:
                tot += int(n)
                n = ''
    if n:
        tot += int(n)
    return tot

