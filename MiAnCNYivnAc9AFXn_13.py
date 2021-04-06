
def changeTypes(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], bool):
            lst[i] = not lst[i]        
        elif isinstance(lst[i], int) and lst[i] % 2 == 0:
            lst[i] = lst[i] + 1
        elif isinstance(lst[i], str):
            lst[i] = lst[i].capitalize() + "!"
    return lst

