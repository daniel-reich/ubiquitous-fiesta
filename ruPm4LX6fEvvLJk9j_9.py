
VALUES = {chr(65+i): 10+i for i in range(26)}
for i in range(10):
    VALUES[str(i)] = i
INV_VALUES = {value: key for key, value in VALUES.items()}
​
POWERS = {(base, power): base**power for base in range(1, 37) for power in range(200)}
​
def to_base(d, to_base):
    # convert decimal integer (base 10) to base base_k
    res = ""
    for p in range(50, -1, -1):
        power = POWERS[(to_base, p)]
        m = d // power
        res += INV_VALUES[m]
        d = d % power
    while res[0] == '0':
        res = res[1:]
    return res
​
def esthetic(num):
    L = []
    for base in range(2, 11):
        n = to_base(num, base)
        #print(num, base, n)
        if all([abs(int(n[i]) - int(n[i-1])) == 1 for i in range(1, len(n))]):
            L.append(base)
    return L if len(L) > 0 else "Anti-Esthetic"

