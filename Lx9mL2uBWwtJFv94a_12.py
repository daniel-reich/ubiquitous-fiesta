
def checker_board(n, el1, el2):
    if el1 == el2:
        return "invalid"
    l = [[el1]*n for i in range(n)]
    for i in range(n):
        if (i+2)%2==0:
            for j in range(n):
                if (j+2)% 2 == 1:
                    l[i][j] = el2
        elif (i+2)%2==1:
            for j in range(n):
                if (j+2)% 2 == 0:
                    l[i][j] = el2
    return l

