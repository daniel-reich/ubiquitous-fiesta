
def shuffle_count(num):
    if num == 2:
        return 1
    ctr = 1
    
    while (2**ctr) % (num-1) != 1:
        ctr += 1
    return ctr

