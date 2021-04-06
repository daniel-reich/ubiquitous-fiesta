
POWERS = {(base, power): base**power for base in range(1, 51) for power in range(200)}
​
def to_base(d, to_base, values):
    # convert decimal integer (base 10) to base to_base
    res = []
    for p in range(50, -1, -1):
        power = POWERS[(to_base, p)]
        m = d // power
        res.append(str(values[m]))
        d = d % power
    while res[0] == str(values[0]):
        res.pop(0)
    return ''.join(res)
​
def base_n(base, values, num):
    if len(values) != base:
        return False
    return to_base(num, base, values)

