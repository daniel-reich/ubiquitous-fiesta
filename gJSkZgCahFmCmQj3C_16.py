
def de_nest(lst):
    while type(lst) ==list:
        lst = lst[0]
        if type(lst)==int:
            break
            
    return lst

