
def primorial(n):
    list1 = []
    for i in range(2,100):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            list1.append(i)
    sum1 = 1
    for k in list1[0:n]:
        sum1 *= k
    return sum1

