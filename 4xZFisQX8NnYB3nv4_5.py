
def maximum_seating(lst):
    lst = [0,0] + lst + [0,0] 
    total = 0
    for i in range(2,len(lst)-2):
        if lst[i] == 0:
            if all([lst[i + j] == 0 for j in [1,2,-1,-2]]):
                total += 1
                lst[i] = 1
    return total

