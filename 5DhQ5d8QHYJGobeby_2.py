
import copy
​
def hot_brick(t):
    old = [[25 for _ in range(12)] for _ in range(10)]+[[25]+10*[90]+[25]]
    com = [(i,j) for i in[-1,0,1] for j in [-1,0,1]]
    for _ in range(t):
        new = copy.deepcopy(old)
        for lin in range(1, 10):
            for col in range(1,11):
                soma = 0
                for t in com:
                    soma += old[lin+t[0]][col+t[1]]
                new[lin][col] = round(soma/9)
        old = copy.deepcopy(new)
    return [[old[i][j] for j in range(1,11)] for i in range(1,11)]

