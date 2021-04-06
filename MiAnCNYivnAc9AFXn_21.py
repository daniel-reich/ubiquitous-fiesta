
def change_types(lst):
    new = []
    for i in lst:
        if isinstance(i, str):
            new.append(i.capitalize()+'!')
        elif isinstance(i,bool):
            new.append(not i)
        elif (isinstance(i, int) and i%2==0):
            new.append(i+1)
        else:
            new.append(i)
    return new

