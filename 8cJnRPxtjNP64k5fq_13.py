
def dance(lst,parameter):
    lst_m = [k[1] for k in lst];
    lst_w = [k[0] for k in lst];
    if 'women' in parameter:
        lst_w = lst_w[::-1];
    else:
        lst_m = lst_m[::-1];        
    return [list(a) for a in zip(lst_w,lst_m)]

