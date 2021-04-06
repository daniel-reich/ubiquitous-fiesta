
def get_lucky_number(size, nth):
    temp = []
    for i in range(1,size+1):
        temp.append(i)
    a = 0
    f = temp[1]
​
    while f < len(temp):
        for i in range(len(temp)):
            if (i+1) % f == 0:
                temp[i] = 0
        while 0 in temp:
            temp.remove(0)
        a += 1
        f = temp[a]
    return temp[nth-1]

