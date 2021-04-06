
def box_seq(step):
    count, n = 1, 0
    while count < step + 1:
        if count % 2: n = n + 3
        else: n = n -1
        count += 1
    return n

