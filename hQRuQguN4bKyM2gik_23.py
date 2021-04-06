
def simple_check(a, b):
    count = 0
    if max(a,b) % min(a,b) == 0:
        count += 1
    else:
        count += 0
    while a and b:
        a = a-1
        b = b-1
        if min(a,b) == 0:
            break
        else:
            if max(a,b) % min(a,b) == 0:
                count += 1
    return count

