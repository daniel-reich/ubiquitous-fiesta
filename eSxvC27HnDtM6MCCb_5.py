
def base_n(base, values, num):
    values = [str(i) for i in values]
    if len(values) != base:
        return False
    res = ''
    n = 1
    while base ** (n + 1) < num:
        n += 1
​
    for i in range(n, 0, -1):
        if num >= base**i:
            rem = num % base**i
            amp = int((num - rem)/base**i)
            num -= amp * base**i
            res += values[amp]
        else:
            res += values[0]
​
    return (res + values[num]).lstrip(values[0])

