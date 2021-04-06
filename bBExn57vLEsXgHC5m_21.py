
def same_line(lst):
    if lst[0][0]-lst[1][0] != 0 :
        grad = (lst[0][1]-lst[1][1])/(lst[0][0]-lst[1][0])
        return(lst[2][1] == grad*lst[2][0] + lst[0][1]-grad*lst[0][0])
    return lst[0][0] == lst[2][0]

