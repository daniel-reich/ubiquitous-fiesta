
def arrow(num):
    res = [i * '>' for i in range(1, num + 1)]
    return res + res[:-1][::-1] if num % 2 else res + res[::-1]

