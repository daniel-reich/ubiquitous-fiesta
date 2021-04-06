
def make_dartboard(n):
    if n == 0:
        return []
    result = ["1"] * n
    if n % 2 == 0:
        result[0] = int("1" * n)
        for i in range(1, n // 2):
            result[i] = result[i - 1] + int("1" * (n - 2 * i) + "0" * i)
        for i in range(n // 2, n):
            result[i] = result[n - 1 - i]
    elif n % 2 != 0:
        result[0] = int("1" * n)
        for i in range(1, n // 2 + 1):
            result[i] = result[i - 1] + int("1" * (n - 2 * i) + "0" * i)
        for i in range(n // 2 + 1, n):
            result[i] = result[n - 1 - i]
    return result

