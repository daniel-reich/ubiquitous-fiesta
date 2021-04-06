
def max_product(n):
    result = [(0, 0)]
    for i in range(0, n + 1):
        n = [int(x) for x in str(i)] 
        add = 1
        for j in n:
            add = add * int(j)
        if add > result[0][0]:
            result = [(add, i)]
        elif add == result[0][0]:
            result.append((add, i))
    return [i[1] for i in result]

