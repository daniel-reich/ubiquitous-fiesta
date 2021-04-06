
def is_prob_matrix(lst):
    i = 0
    j = 0
    k = 0
    x = 0
    
    if len(lst) == len(lst[0]):
        pass
    else:
        return False
    
    while i < len(lst):
        for j in range(len(lst[j])):
            if 0 <= lst[i][j] <= 1:
                j += 1
            else:
                return False
        j = 0
        i += 1
    
    while k < len(lst):
        if sum(lst[k]) == 1.0:
            x += 1
            k += 1
        else:
            k += 1
    if x == len(lst):
        return True
    else:
        return False

