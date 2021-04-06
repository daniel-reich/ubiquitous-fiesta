
def can_traverse(x):
    a = []
    for y in range(0,len(x[0])):
        counter = 0
        for i in range(0,len(x)):
            if x[i][y] == 1:
                counter += 1
        a.append(counter)
    for i in range(0,len(a)):
        if i != 0:
            if a[i-1]-a[i] == -1 or a[i-1]-a[i] == 1 or a[i-1]-a[i] == 0:
                continue
            else:
                return False
                
    return True

