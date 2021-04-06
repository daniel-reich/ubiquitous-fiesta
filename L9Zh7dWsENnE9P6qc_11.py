
def finished(x):
    count = 0
    for i in range(len(x)):
        if x[i] == 1:
            count += 1
    if count == 1:
        return True
    else:
        return False
​
def find_next(x, a):
    found = False
    index = a + 1
    while found == False:
        if x[index % len(x)] == 1:
            found = True
            return index % len(x)
        else:
            index += 1
​
def josephus(n):
    x = [1 for i in range(n)]
    while finished(x) == False:
        for i in range(len(x)):
            if x[i] == 1:
                x[find_next(x,i)] = 0
    return find_next(x,0) + 1

