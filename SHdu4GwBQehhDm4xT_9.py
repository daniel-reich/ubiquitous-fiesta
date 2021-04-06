
def freed_prisoners(prison):
    index = 0
    freed = 0
    if prison[0] == 0:
        return 0
            
    while index < len(prison):
        if prison[index] == 1:
            freed += 1
            prison = [abs(i - 1) for i in prison]
        else:
            index += 1
    
    return freed

