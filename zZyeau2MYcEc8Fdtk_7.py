
def round_number(num, n):
    check = num / n
    high = (int(check) + 1) * n
    low = (int(check)) * n
    
    if num - low < abs(num - high):
        return low
    else:
        return high

