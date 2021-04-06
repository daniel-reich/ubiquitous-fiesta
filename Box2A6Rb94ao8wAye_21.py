
def leader(lst):
    
    new_list = []
    
    while len(lst)!= 0:
        
        lst = lst[lst.index(max(lst)):]
        
        new_list.append(lst.pop(0))
        
    return new_list

