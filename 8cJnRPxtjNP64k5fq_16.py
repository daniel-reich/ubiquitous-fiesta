
def dance(lst, parameter):
    men = [lst[i][1] for i in range(len(lst))][::-1]
    wom = [lst[i][0] for i in range(len(lst))]
    lst1 = [[i,j] for i,j in zip(wom,men)]
    return lst1 if parameter=="men" else lst1[::-1]

