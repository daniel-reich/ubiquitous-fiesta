
def make_dartboard(n):
    m = n // 2 + n % 2
    s = ["1" * m]
    for i in range(1, m):
        add = s[-1][: i] + (m - i) * str(i + 1)
        s.append(add)
    if n % 2 == 1:
        s = [i[:-1] + i[::-1] for i in s]
        s = s[:-1] + s[::-1]
    else: 
        s = [i + i[::-1] for i in s]
        s = s + s[::-1]
    return [int(i) for i in s]

