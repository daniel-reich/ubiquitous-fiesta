
def jazzify(lst):
    for i in range(len(lst)):
        if lst[i][-1] != '7':
            lst[i] = lst[i] + '7'
    return(lst)

