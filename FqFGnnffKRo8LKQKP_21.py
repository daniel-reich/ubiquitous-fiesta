
def simple_numbers(a, b):
    res = []
    for num in range(a, b + 1):
        c = sum(int(n)**idx for idx, n in enumerate(str(num), 1))
        if c == num:  res.append(num)
    return res

