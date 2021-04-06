
def possible_path(lst):
    if len(lst)==1:
        return True;
    for i in range(len(lst)-1):
        if type(lst[i])==int and type(lst[i+1])==int:
            return False;
    return True;

