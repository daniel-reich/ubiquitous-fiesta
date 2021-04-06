
import bisect
​
n = 10000
m0 = 10.0
r = 0.1 / n
dt = 1. / n
t = 0
S = 10.
f = 0.1 / n
​
T, Salt = [], []
while t <= 150:
    t += dt
    S = S - f * S + r
    T.append(t)
    Salt.append(S)
​
def salt(t):
    idx = bisect.bisect_left(T, t)
    rem = Salt[idx]
    return round(rem, 3)

