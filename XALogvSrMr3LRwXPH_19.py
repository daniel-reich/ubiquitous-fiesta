
def is_shuffled_well(lst):
    
    consecutive_count = 0
    
    for cnt, i in enumerate(lst):
        if i == lst[cnt-1] + 1:
            consecutive_count+=1
            if consecutive_count ==2:
                return False
        else:
            consecutive_count = 0
    
    for cnt, i in enumerate(lst):
        if i == lst[cnt-1] - 1:
            consecutive_count += 1
            if consecutive_count == 2:
                return False
        else:
            consecutive_count = 0
            
    return True

