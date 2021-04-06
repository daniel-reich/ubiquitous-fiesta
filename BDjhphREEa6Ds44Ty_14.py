
import math
​
eps = 1e-1
v = 0.343
​
def dist(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
​
def bomb(lst):
    X, Y, T = [], [], []
    for x, y, t in lst:
        X.append(x)
        Y.append(y)
        T.append(t)
    for bx in range(51):
        for by in range(51):
            found = True
            for i in range(3):
                d = dist((bx, by), (X[i], Y[i]))
                if abs(d / v - T[i]) > eps:
                    found = False
                    break
            if found:
                return (bx, by)

