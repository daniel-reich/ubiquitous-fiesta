
def final_result(lst):
    i = 0
    pop = False
    while i < len(lst)-1:
        if lst[i] == lst[i+1]:
            pop = True
            lst.pop(i)
        else:
            if pop:
                lst.pop(i)
                pop = False
                i = 0
            else:
                i += 1
    return lst[:-1] if pop else lst

