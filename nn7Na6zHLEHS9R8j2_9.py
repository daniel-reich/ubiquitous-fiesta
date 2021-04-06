
def deep_count(lst):
    count = 0
    
    for elem in lst:
        if isinstance(elem, list):
            count+=1
            
            count+=deep_count(elem)
            
            
        else:
            count += 1
    return count

