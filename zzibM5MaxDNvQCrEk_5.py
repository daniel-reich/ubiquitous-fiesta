
def will_fit(holds, cargo):
    s1 = 0
    s2 = 0
    for i in range(len(holds)):
        if holds[i] == 'S':
            s1+= 50
        elif holds[i] == 'M':
            s1+=100
        elif holds[i] == 'L':
            s1+= 200
    for j in range(len(cargo)):
        s2+= cargo[j]
    if s1 >=s2:
        return True
    else:
        return False

