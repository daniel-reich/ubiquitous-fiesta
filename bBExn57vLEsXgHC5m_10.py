
def same_line(lst):
    try:
        m = (lst[1][1]-lst[0][1])/(lst[1][0]-lst[0][0])
    except:
            if lst[0][0] == lst[1][0] == lst[2][0]:
                return True
            else:
                return False
    c = lst[0][1]-m*lst[0][0]
    y = lst[2][1]
    x = lst[2][0]
    return y == m*x+c

