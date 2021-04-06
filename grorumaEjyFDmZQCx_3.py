
def is_wristband(lst):
    diagonal_left=[]
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if i>0 and j>0:
                if lst[i][j]==lst[i-1][j-1]:
                    diagonal_left.append(True)
​
    diagonal_right=[]
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if i>0 and j>0:
                if lst[::-1][i][j]==lst[::-1][i-1][j-1]:
                    diagonal_right.append(True)
​
​
    is_horizontal=[]
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if j!=0 and lst[i][j]==lst[i][j-1]:
                is_horizontal.append(True)
​
    is_vertical=[]
​
    for j in range(len(lst[0])):
        for i in range(len(lst)):
            if i!=0 and lst[i][j]==lst[i-1][j]:
                is_vertical.append(True)
    if sum(is_horizontal)==(i+1)*(j):
        return True
    elif sum(is_vertical)==i*(j+1):
        return True
​
    elif sum(diagonal_left)==i*j:
        return True
    elif sum(diagonal_right)==i*j:
        return True
    else:
        return False

