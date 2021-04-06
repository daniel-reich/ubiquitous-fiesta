
def upward_trend (lst) :
    for x in range(len(lst)-1) :
        if lst[x] == str(lst[x]) or lst[x+1] == str(lst[x+1]) :
            return "Strings not permitted!"
        elif lst[x] > lst[x+1] :
            return False
    return True

