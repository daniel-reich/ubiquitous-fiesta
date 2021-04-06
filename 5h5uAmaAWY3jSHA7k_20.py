
def landscape_type(lst):
    for i in range(1, len(lst)-1):
        
        if max(lst[:i] + lst[i+1:]) < lst[i]:
            if lst[:i] == sorted(lst[:i]) and lst[i+1:] == sorted(lst[i+1:], reverse = True):
                return 'mountain'
            
        if min(lst[:i] + lst[i+1:]) > lst[i]:
            if lst[:i] == sorted(lst[:i], reverse = True) and lst[i+1:] == sorted(lst[i+1:]):
                return 'valley'
            
    return 'neither'

