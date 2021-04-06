
def is_shuffled_well(lst):
    holder = []
    for i in range(len(lst) - 2):
        if lst[i + 1] == lst[i] + 1 and lst[i + 2] == lst[i + 1] + 1:
            holder.append(False)
            
        elif lst[i + 1] == lst[i] - 1 and lst[i + 2]  == lst[i + 1] - 1:
            holder.append(False)
        
        else:
            holder.append(True)
        
    if sum(holder) == len(lst) - 2:
        return True
    
    else:
        return False

