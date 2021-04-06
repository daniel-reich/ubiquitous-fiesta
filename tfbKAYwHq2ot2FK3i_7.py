
def non_repeats(base):
    count = 0
    for i in range(1, base+1):
        current = base -1
        for j in range(1,i):
            current = current*(base - j)
        count = count + current
    return count

