
VALUES = {chr(97+i): i for i in range(26)}
INV_VALUES = {value: key for key, value in VALUES.items()}
​
POWERS = {(base, power): base**power for base in range(1, 37) for power in range(200)}
​
def from_base(k, base_k):
    # convert integer k in base base_k to decimal (base 10)
    L = len(k)
    res = 0
    for i in range(L - 1, -1, -1):
        res += VALUES[k[i]] * POWERS[(base_k, L - 1 - i)]
    return res
​
def to_base(d, to_base):
    # convert decimal integer (base 10) to base base_k
    res = ""
    for p in range(50, -1, -1):
        power = POWERS[(to_base, p)]
        m = d // power
        res += INV_VALUES[m]
        d = d % power
    while res[0] == 'a':
        res = res[1:]
    return res
​
def base_conv(n,b):
    if type(n) == int:
        ans = to_base(n, b)
        return ans
    L = [ord(c) - 97 for c in n]
    if min(L) < 0 or max(L) >= b:
        return n + " is not a base " + str(b) + " number."
    ans = from_base(n, b)
    return ans

