
def digit_distance(v, k):
    r = 0
    a = list(zip(str(v),str(k)))
    for i in range(len(a)):
        r += abs(int(a[i][0])-int(a[i][1]))
    return r

