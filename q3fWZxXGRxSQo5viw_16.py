
def cal(depth):
    minute = 0
    rest = 0
    if depth<=5:
        return 1
    else:
        while depth>0:
            depth -= 5
            minute += 1
            if (minute-10*rest)%30 == 0 and depth>0:
                depth += 30
                minute += 10
                rest += 1
    return minute

