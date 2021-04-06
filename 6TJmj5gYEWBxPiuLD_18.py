
def seating_students(l):
    s = 0
    l_r = [True for i in range(l[0]//2)]
    l_l = [True for i in range(l[0]//2)]
    for i in l[1:]:
        if i%2 == 0 :
            l_r[i//2-1] = False
        else:
            l_l[i//2] = False
    for i in range(len(l_r)-1):
        if l_l[i] == l_l[i+1] == True:
            s += 1
        if l_r[i] == l_r[i+1] == True:
            s += 1
        if l_l[i] == l_r[i] == True:
            s += 1
    if l_r[-1] == l_l[-1] == True:
        s += 1
    return s

