
def flip_list(lst):
    new = []
    if len(lst) == 0:
        return lst
    elif type(lst[0]) != list:
        for i in lst:
            new.append([i])
        return new
    else:
        for ind in range(len(lst)):
            new.append(lst[ind][0])
        return new

