
def upward_trend(lst):
    for i in lst:
        if type(i) == str:
            return "Strings not permitted!"
    
    bool_lst = [lst[i]<lst[i+1] for i in range(len(lst)-1)]
    if False in bool_lst:
        return False
​
    return True

